from watchdog.events import FileSystemEventHandler
import os
import tkinter as tk
import shutil
import subprocess
from tkinter import messagebox
from tkinter import simpledialog

# chemin des différents dossier wallpaper, image, document, code et zip
WALLPAPER_DIR = r"C:\Users\dksll\Pictures\wallpaper"
IMAGES_DIR = r"C:\Users\dksll\Pictures"
DOCUMENT_DIR = r"C:\Users\dksll\Documents"
CODE_DIR = r"C:\Users\dksll\Documents\code"
ZIP_DIR = r"C:\Users\dksll\Documents\zip"

""" class : OrganizerHandler
        description : class qui a pour but de gérer l'ajout d'un fichier dans le dossier download
            détécté par le watchdog que se soit un fichier image, code, document ou zip
        paramètres : FileSystemEventHandler : événement déclenché par le watchdog
"""


class OrganizerHandler(FileSystemEventHandler):
    """fonction : on_created
    description : vérifie quel fonction activer en fonction du fichier récupérer par l'évenement watchdog
    paramètres : event : événement déclenché par le watchdog
    sortie : null
    """

    def on_created(self, event):
        # vérifie si ce n'est pas un dossier
        if not event.is_directory:
            # vérifie si fichier est image
            if self.is_image(event.src_path):
                self.prompt_user_for_action(event.src_path)
            # vérifie si fichier est document
            elif self.is_doc(event.src_path):
                self.prompt_user_for_action_doc(event.src_path)
            # vérifie si fichier est code
            elif self.is_code(event.src_path):
                self.prompt_user_for_action_code(event.src_path)
            # vérifie si fichier est zip
            elif self.is_zip(event.src_path):
                self.prompt_user_for_action_zip(event.src_path)

    """ fonction : is_image
        description : vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier image
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : booléen : vraie si fichier est image faux si fichier n'est pas image
    """

    def is_image(self, file_path):
        # Liste d'extension d'image
        image_extensions = {
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".bmp",
            ".tiff",
            ".webapp",
        }
        # séparation du nom complet du fichier afin de récupérer uniquement l'extension
        ext = os.path.splitext(file_path)[1].lower()
        # renvoie du booléen qui vérifie si l'extension du fichier de file_path n'est pas dans la liste
        return ext in image_extensions

    """ fonction : is_zip
        description : vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier zip
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : booléen : vraie si fichier est zip faux si fichier n'est pas zip
    """

    def is_doc(self, file_path):
        # Liste d'extension de document
        doc_extensions = {
            ".pdf",
            ".doc",
            ".docx",
            ".odt",
            ".ods",
            ".odp",
            ".txt",
            ".wpd",
            ".wps",
        }
        ext = os.path.splitext(file_path)[1].lower()
        return ext in doc_extensions

    """ fonction : is_code
        description : vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier code
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : booléen : vraie si fichier est code faux si fichier n'est pas code
    """

    def is_code(self, file_path):
        # liste d'extension de code
        code_extensions = {
            ".py",
            ".c",
            ".cpp",
            ".cs",
            ".java",
            ".jar",
            ".php",
            ".css",
            ".html",
        }
        ext = os.path.splitext(file_path)[1].lower()
        return ext in code_extensions

    """ fonction : is_zip
        description : vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier zip
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : booléen : vraie si fichier est zip faux si fichier n'est pas zip
    """

    def is_zip(self, file_path):
        # Liste d'extension de zip
        zip_extensions = {".zip", ".7z", ".tar.gz"}
        ext = os.path.splitext(file_path)[1].lower()
        return ext in zip_extensions

    """ fonction : prompt_user_for_action_code
        description : demander a l'utilisateur si il veut déplacer le fichier code dans un sous dossier du nom du fichier
            dans le dossier code,
            si il veut déplacer le fichier dans un sous dossier du dossier code déjà existant
            ou si il veut le faire manuellement
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : aucun
    """

    def prompt_user_for_action_code(self, file_path):
        # Initialisation de la fenetre tkinter
        root = tk.Tk()
        root.withdraw()

        # construction des choix de l'utilisateurs via des radiobutton
        option = tk.IntVar()
        top = tk.Toplevel(root)
        top.title("Choisir une option")
        tk.Label(top, text="ou déplacer le fichier?").pack(anchor=tk.W)
        tk.Radiobutton(
            top, text="1: dossier code(créer nouveau dossier)", variable=option, value=1
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            top,
            text="2: dossier code(mettre dans un dossier existant)",
            variable=option,
            value=2,
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            top, text="3: Autre (déplacer manuellement)", variable=option, value=3
        ).pack(anchor=tk.W)
        tk.Button(top, text="OK", command=top.quit).pack()

        # gérer lorsque l'utilisateur appuie sur la croix
        def on_close():
            root.destroy()

        top.protocol("WM_DELETE_WINDOW", on_close)
        # placer la fenetre au centre de l'écran
        root.eval(f"tk::PlaceWindow {str(top)} center")
        # mettre la fenetre a la bonne taille
        top.geometry("300x140")
        # faire en sorte que la fenetre aparaisse devant toute les autres
        top.wm_attributes("-topmost", True)

        # ajout de la fenetre au mainloop
        top.mainloop()

        # récuparation de l'option choisi par l'utilisateur
        selected_option = option.get()

        # si option 1 on déplace le fichier dans un nouveau dossier créer dans le dossier code
        if selected_option == 1:
            # fonction de création + déplacer fichier
            self.move_file_create_dir(file_path, CODE_DIR)
            # on détruit la fenetre pour éviter d'autre bug si on la relance
            root.destroy()
        # si option 2 on demande a l'utilisateur dans quel sous dossier du dossier code il veut mettre le fichier
        elif selected_option == 2:
            # on détruit la premiére fenetre car on en fait apparaitre une deuxième
            root.destroy()
            # fonction qui prompt l'utilisateur dans quel sous dossier il veut déplacer le fichier + déplacement
            self.move_file_project(file_path, CODE_DIR)
        # si option 3 on ouvre l'explorateur de fichier car l'utilisateur veut déplacer manuellement le fichier
        elif selected_option == 3:
            # ca marche le file explorer est afficher
            self.open_file_explorer_and_prompt(file_path)
            root.destroy()

        root.quit()

    """ fonction : prompt_user_for_action_zip
        description : demander a l'utilisateur si il veut déplacer le fichier zip dans un sous dossier du dossier zip
            qui porte le nom du fichier zip,
            si il veut déplacer le fichier zip dans un sous dossier déjà existant du dossier zip
            ou si il veut le faire manuellement
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : aucun
    """

    def prompt_user_for_action_zip(self, file_path):
        # Initialize tkinter root window
        root = tk.Tk()
        root.withdraw()

        # Present the user with options using radiobuttons
        option = tk.IntVar()
        top = tk.Toplevel(root)
        top.title("Choisir une option")
        tk.Label(top, text="ou déplacer le fichier?").pack(anchor=tk.W)
        tk.Radiobutton(
            top, text="1: dossier zip(créer nouveau dossier)", variable=option, value=1
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            top,
            text="2: dossier zip(mettre dans un dossier existant)",
            variable=option,
            value=2,
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            top, text="3: Autre (déplacer manuellement)", variable=option, value=3
        ).pack(anchor=tk.W)
        tk.Button(top, text="OK", command=top.quit).pack()

        def on_close():
            root.destroy()

        top.protocol("WM_DELETE_WINDOW", on_close)
        root.eval(f"tk::PlaceWindow {str(top)} center")
        top.geometry("300x140")
        top.wm_attributes("-topmost", True)

        top.mainloop()

        selected_option = option.get()

        if selected_option == 1:
            # ca marche le fichier est déplacer dans le bon dossier
            self.move_file_create_dir(file_path, ZIP_DIR)
            root.destroy()
        elif selected_option == 2:
            # ca marche le fichier est déplacer dans le bon dossier
            root.destroy()
            self.move_file_project(file_path, ZIP_DIR)
        elif selected_option == 3:
            # ca marche le file explorer est afficher
            self.open_file_explorer_and_prompt(file_path)
            root.destroy()

        root.quit()

    """ fonction : prompt_user_for_action_doc
        description : demander a l'utilisateur si il veut déplacer le fichier document dans le dossier document
            ou si il veut le faire manuellement
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : aucun
    """

    def prompt_user_for_action_doc(self, file_path):
        root = tk.Tk()
        root.withdraw()

        option = tk.IntVar()
        top = tk.Toplevel(root)
        top.title("Choisir une option")
        tk.Label(top, text="ou déplacer le fichier?").pack(anchor=tk.W)
        tk.Radiobutton(
            top,
            text="1: dossier documents(créer un nouveau dossier)",
            variable=option,
            value=1,
        ).pack(anchor=tk.W)
        tk.Radiobutton(
            top, text="2: Autre (déplacer manuellement)", variable=option, value=2
        ).pack(anchor=tk.W)
        tk.Button(top, text="OK", command=top.quit).pack()

        def on_close():
            root.destroy()

        top.protocol("WM_DELETE_WINDOW", on_close)
        root.eval(f"tk::PlaceWindow {str(top)} center")
        top.geometry("300x140")
        top.wm_attributes("-topmost", True)

        top.mainloop()

        selected_option = option.get()

        # si option 1 on déplace le fichier dans un sous dossier du nom du fichier dans le dossier document
        if selected_option == 1:
            self.move_file_create_dir(file_path, DOCUMENT_DIR)
            root.destroy()
        elif selected_option == 2:
            self.open_file_explorer_and_prompt(file_path)
            root.destroy()

        root.quit()

    """ fonction : prompt_user_for_action
        description : demander a l'utilisateur si il veut déplacer le fichier image dans le dossier wallpaper,
            le dossier image
            ou si il veut le faire manuellement
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download
        sortie : aucun
    """

    def prompt_user_for_action(self, file_path):
        root = tk.Tk()
        root.withdraw()

        option = tk.IntVar()
        top = tk.Toplevel(root)
        top.title("Choisir une option")
        tk.Label(top, text="ou déplacer le fichier?").pack(anchor=tk.W)
        tk.Radiobutton(top, text="1: dossier wallpaper", variable=option, value=1).pack(
            anchor=tk.W
        )
        tk.Radiobutton(top, text="2: dossier images", variable=option, value=2).pack(
            anchor=tk.W
        )
        tk.Radiobutton(
            top, text="3: Autre (déplacer manuellement)", variable=option, value=3
        ).pack(anchor=tk.W)
        tk.Button(top, text="OK", command=top.quit).pack()

        def on_close():
            root.destroy()

        top.protocol("WM_DELETE_WINDOW", on_close)
        root.eval(f"tk::PlaceWindow {str(top)} center")
        top.geometry("300x140")
        top.wm_attributes("-topmost", True)

        top.mainloop()

        selected_option = option.get()

        # si option 1 on déplace le fichier dans le dossier wallpaper
        if selected_option == 1:
            # fonction qui déplace le fichier dans le dossier de destination ici wallpaper
            self.move_file(file_path, WALLPAPER_DIR)
            root.destroy()
        # si option 2 on déplace le fichier dans le dossier image
        elif selected_option == 2:
            # fonction qui déplace le fichier dans le dossier de destination ici image
            self.move_file(file_path, IMAGES_DIR)
            root.destroy()
        elif selected_option == 3:
            self.open_file_explorer_and_prompt(file_path)
            root.destroy()

        root.quit()

    """ fonction : move_file
        description : déplacer un fichier contenu dans file_path vers le dossier de destination contenu dans destination_dir
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download,
            destination_dir : chemin du dossier de destination
        sortie : aucun
    """

    def move_file(self, file_path, destination_dir):
        # récupération du nom du fichier
        file_name = os.path.basename(file_path)
        # nouveau chemin créer a partir du nom de fichier et le dossier de destination
        new_path = os.path.join(destination_dir, file_name)
        # déplacer le fichier dans le nouveau chemin
        shutil.move(file_path, new_path)

    """ fonction : move_file_create_dir
        description : déplacer un fichier contenu dans file_path dans un sous dossier portant le meme nom que le fichier
            dans le dossier de destination contenu dans destination_dir
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download,
            destination_dir : chemin du dossier de destination
        sortie : aucun
    """

    def move_file_create_dir(self, file_path, destination_dir):
        file_name = os.path.basename(file_path)

        # récupération du nom du fichier sans l'extension
        file_name_without_ext = os.path.splitext(file_name)[0]

        # nouveau chemin créer a partir du nom de fichier sans extension et du dossier de destination
        new_dir_path = os.path.join(destination_dir, file_name_without_ext)
        # création du sous dossier dans le dossier de destination ayant le nom du fichier sans extension
        os.makedirs(new_dir_path, exist_ok=True)

        # nouveau chemin créer a partir du nom de fichier et le dossier de destination
        new_file_path = os.path.join(new_dir_path, file_name)

        # déplacer le fichier dans le nouveau chemin
        shutil.move(file_path, new_file_path)

    """ fonction : move_file_project
        description : déplacer un fichier contenu dans file_path vers un sous dossier contenu dans une liste des dossier
            dans le dossier de destination contenu dans destination_dir 
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download,
            destination_dir : chemin du dossier de destination
        sortie : aucun
    """

    def move_file_project(self, file_path, destination_dir):

        # récupérer une liste de tous les sous dossier contenu dans le dossier de destination
        dirs = [
            d
            for d in os.listdir(destination_dir)
            if os.path.isdir(os.path.join(destination_dir, d))
        ]

        # message d'erreur si aucun dossier n'a été trouvé
        if not dirs:
            messagebox.showerror(
                "Erreur", "Aucun dossier trouvé dans le dossier de destination."
            )
            return

        root = tk.Tk()
        root.withdraw()

        # Affiche une fenetre tkinter qui demande a l'utilisateur quel dossier il veut choisir et affiche la liste de sous dossier
        selected_dir = simpledialog.askstring(
            "Séléctionner le dossier", f"Choissisez un dossier parmi la liste: {dirs}"
        )

        # si le dossier choisi est dans la liste de dossier déplacer le fichier dans le sous dossier
        if selected_dir in dirs:
            # Move the file to the selected directory
            destination_path = os.path.join(
                destination_dir, selected_dir, os.path.basename(file_path)
            )
            try:
                shutil.move(file_path, destination_path)
                messagebox.showinfo(
                    "Succée", f"Fichier déplacer dans {destination_path}"
                )
            except Exception as e:
                messagebox.showerror("Erreur", f"Échec du déplacement de fichier: {e}")
        else:
            messagebox.showerror("Erreur", "Dossier invalide ou séléction annuler.")

        # déstruction de la fenetre pour éviter les bug quand on relance une fenetre
        root.destroy()

    """ fonction : open_file_explorer_and_prompt
        description : ouvrir l'explorateur du fichier a l'endroit ou se trouve le fichier
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download,
        sortie : aucun
    """

    def open_file_explorer_and_prompt(self, file_path):
        # Ouverture du dossier dans l'explorateur du fichier a l'endroit ou se trouve le fichier
        file_dir = os.path.dirname(file_path)
        if os.name == "nt":  # Windows
            subprocess.Popen(f'explorer /select,"{file_path}"')
        elif os.name == "posix":  # macOS or Linux
            subprocess.Popen(
                ["open", file_dir]
                if sys.platform == "darwin"
                else ["xdg-open", file_dir]
            )
