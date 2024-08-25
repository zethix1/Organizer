from watchdog.events import FileSystemEventHandler
import os
import tkinter as tk
import shutil
import subprocess
from tkinter import messagebox
from tkinter import simpledialog
from pathlib import Path
from FolderInitializationError import FolderInitializationError

pictures_dir = Path.home() / "Pictures"
documents_dir = Path.home() / "Documents"

# Chemin des différents dossier wallpaper, image, document, code et zip
WALLPAPER_DIR = pictures_dir / "wallpaper"
IMAGES_DIR = pictures_dir
DOCUMENT_DIR = documents_dir
CODE_DIR = documents_dir / "Code"
ZIP_DIR = documents_dir / "Zip"

""" class : OrganizerHandler
        description : Class qui a pour but de gérer l'ajout d'un fichier dans le dossier download
            détécté par le watchdog que se soit un fichier image, code, document ou zip
        paramètres : FileSystemEventHandler : Événement déclenché par le watchdog
"""


class OrganizerHandler(FileSystemEventHandler):
    """fonction : on_created
    description : Vérifie quel fonction activer en fonction du fichier récupérer par l'évenement watchdog
    paramètres : event : Événement déclenché par le watchdog
    sortie : NULL
    """

    def on_created(self, event):
        try:
            # Vérifie si ce n'est pas un dossier
            if not event.is_directory:
                # Vérifie si fichier est image
                if self.is_image(event.src_path):
                    self.prompt_user_for_action(event.src_path)
                # Vérifie si fichier est document
                elif self.is_doc(event.src_path):
                    self.prompt_user_for_action_doc(event.src_path)
                # Vérifie si fichier est code
                elif self.is_code(event.src_path):
                    self.prompt_user_for_action_code(event.src_path)
                # Vérifie si fichier est zip
                elif self.is_zip(event.src_path):
                    self.prompt_user_for_action_zip(event.src_path)
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de vérification du fichier: {e}")
            
    def folder_init(self, folder_path: Path) -> bool:
        """Vérifie si le dossier existe, sinon le crée."""
        try:
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
            return True
        except Exception:
            return False

    """ fonction : is_image
        description : Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier image
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : booléen : Vraie si fichier est image faux si fichier n'est pas image
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
        try:
            # Séparation du nom complet du fichier afin de récupérer uniquement l'extension
            ext = os.path.splitext(file_path)[1].lower()
            # Renvoie un booléen qui vérifie si l'extension du fichier de file_path n'est pas dans la liste
            # (faux si il n'est pas dans la liste et vraie si il est dans la liste)
            return ext in image_extensions
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de séparation du nom de fichier: {e}")
        return False

    """ fonction : is_zip
        description : Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier zip
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : booléen : Vraie si fichier est zip faux si fichier n'est pas zip
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
        try:
            ext = os.path.splitext(file_path)[1].lower()
            return ext in doc_extensions
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de séparation du nom de fichier: {e}")
        return False
    
    """ fonction : is_code
        description : Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier code
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : booléen : Vraie si fichier est code faux si fichier n'est pas code
    """

    def is_code(self, file_path):
        # Liste d'extension de code
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
        try:
            ext = os.path.splitext(file_path)[1].lower()
            return ext in code_extensions
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de séparation du nom de fichier: {e}")
        return False

    """ fonction : is_zip
        description : Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier zip
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : booléen : Vraie si fichier est zip faux si fichier n'est pas zip
    """

    def is_zip(self, file_path):
        # Liste d'extension de zip
        zip_extensions = {
            ".zip",
            ".7z",
            ".tar.gz"
        }
        try:
            ext = os.path.splitext(file_path)[1].lower()
            return ext in zip_extensions
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de séparation du nom de fichier: {e}")
        return False

    """ fonction : prompt_user_for_action_code
        description : Demander a l'utilisateur si il veut déplacer le fichier code dans un sous dossier du nom du fichier
            dans le dossier code,
            si il veut déplacer le fichier dans un sous dossier du dossier code déjà existant
            ou si il veut le faire manuellement
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : NULL
    """

    def prompt_user_for_action_code(self, file_path):
        try:
            # Initialisation de la fenetre tkinter
            root = tk.Tk()
            root.withdraw()

            # Construction des choix de l'utilisateurs via des radiobutton
            option = tk.IntVar()
            top = tk.Toplevel(root)
            top.title("Choisir une option")
            tk.Label(top, text="Ou voulez vous déplacez le fichier?").pack(anchor=tk.W)
            tk.Radiobutton(
                top, text="1: Dossier code(créer nouveau dossier)", variable=option, value=1
            ).pack(anchor=tk.W)
            tk.Radiobutton(
                top,
                text="2: Dossier code(mettre dans un dossier existant)",
                variable=option,
                value=2,
            ).pack(anchor=tk.W)
            tk.Radiobutton(
                top, text="3: Autre (déplacer manuellement)", variable=option, value=3
            ).pack(anchor=tk.W)
            tk.Button(top, text="OK", command=top.quit).pack()

            # Gérer lorsque l'utilisateur appuie sur la croix
            def on_close():
                root.destroy()

            top.protocol("WM_DELETE_WINDOW", on_close)
            # Place la fenetre au centre de l'écran
            root.eval(f"tk::PlaceWindow {str(top)} center")
            # Mettre la fenetre a la bonne taille
            top.geometry("300x140")
            # Faire en sorte que la fenetre aparaisse devant toute les autres
            top.wm_attributes("-topmost", True)

            # Ajout de la fenetre au mainloop
            top.mainloop()
            
        # Gestion d'erreur de la création de la fenêtre de code
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de création de la fenêtre de code: {e}")
            
        try:
            # Récupération de l'option choisi par l'utilisateur
            selected_option = option.get()

            # Si option 1 on déplace le fichier dans un nouveau dossier créer dans le dossier code
            if selected_option == 1:
                if self.folder_init(CODE_DIR):
                    # Fonction de création + déplacer fichier
                    self.move_file_create_dir(file_path, CODE_DIR)
                    # On détruit la fenetre pour éviter d'autre bug si on la relance
                    root.destroy()
                    messagebox.showinfo(
                        "Succès", f"Fichier déplacer dans {CODE_DIR}"
                    )
                else:
                    raise FolderInitializationError(CODE_DIR)
            # Si option 2 on demande a l'utilisateur dans quel sous dossier du dossier code il veut mettre le fichier
            elif selected_option == 2:
                if self.folder_init(CODE_DIR):
                    # On détruit la premiére fenetre car on en fait apparaitre une deuxième
                    root.destroy()
                    # Fonction qui prompt l'utilisateur dans quel sous dossier il veut déplacer le fichier + déplacement
                    self.move_file_project(file_path, CODE_DIR)
                    messagebox.showinfo(
                        "Succès", f"Fichier déplacer dans {CODE_DIR}"
                    )
                else:
                    raise FolderInitializationError(CODE_DIR)
            # Si option 3 on ouvre l'explorateur de fichier car l'utilisateur veut déplacer manuellement le fichier
            elif selected_option == 3:
                # Fonction qui ouvre le file explorer
                self.open_file_explorer_and_prompt(file_path)
                # On détruit la fenetre pour éviter d'autre bug si on la relance
                root.destroy()
                messagebox.showinfo(
                    "Succès", f"Ouverture de l'explorateur de fichier réussie"
                )
        # Gestion d'erreur de la récupération de la séléction de la fenêtre de code
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de récupération de la séléction pour la fenêtre de code: {e}")

        root.quit()

    """ fonction : prompt_user_for_action_zip
        description : Demander a l'utilisateur si il veut déplacer le fichier zip dans un sous dossier du dossier zip
            qui porte le nom du fichier zip,
            si il veut déplacer le fichier zip dans un sous dossier déjà existant du dossier zip
            ou si il veut le faire manuellement
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : NULL
    """

    def prompt_user_for_action_zip(self, file_path):
        try:
            root = tk.Tk()
            root.withdraw()

            option = tk.IntVar()
            top = tk.Toplevel(root)
            top.title("Choisir une option")
            tk.Label(top, text="Ou voulez vous déplacez le fichier?").pack(anchor=tk.W)
            tk.Radiobutton(
                top, text="1: Dossier zip(créer nouveau dossier)", variable=option, value=1
            ).pack(anchor=tk.W)
            tk.Radiobutton(
                top,
                text="2: Dossier zip(mettre dans un dossier existant)",
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
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de création de la fenêtre de zip: {e}")

        try:
            selected_option = option.get()

            if selected_option == 1:
                if self.folder_init(ZIP_DIR):
                    self.move_file_create_dir(file_path, ZIP_DIR)
                    root.destroy()
                    messagebox.showinfo(
                        "Succès", f"Fichier déplacer dans {ZIP_DIR}"
                    )
                else:
                    raise FolderInitializationError(ZIP_DIR)
            elif selected_option == 2:
                if self.folder_init(ZIP_DIR):
                    root.destroy()
                    self.move_file_project(file_path, ZIP_DIR)
                else:
                    raise FolderInitializationError(ZIP_DIR)
            elif selected_option == 3:
                self.open_file_explorer_and_prompt(file_path)
                root.destroy()
                messagebox.showinfo(
                    "Succès", f"Ouverture de l'explorateur de fichier réussie"
                )
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de récupération de la séléction pour la fenêtre de zip: {e}")
        root.quit()

    """ fonction : prompt_user_for_action_doc
        description : Demander a l'utilisateur si il veut déplacer le fichier document dans le dossier document
            ou si il veut le faire manuellement
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : NULL
    """

    def prompt_user_for_action_doc(self, file_path):
        try:
            root = tk.Tk()
            root.withdraw()

            option = tk.IntVar()
            top = tk.Toplevel(root)
            top.title("Choisir une option")
            tk.Label(top, text="Ou voulez vous déplacez le fichier?").pack(anchor=tk.W)
            tk.Radiobutton(
                top,
                text="1: Dossier documents(créer un nouveau dossier)",
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
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de création de la fenêtre de document: {e}")
        
        try:
            selected_option = option.get()

            if selected_option == 1:
                if self.folder_init(DOCUMENT_DIR):
                    self.move_file_create_dir(file_path, DOCUMENT_DIR)
                    root.destroy()
                    messagebox.showinfo(
                        "Succès", f"Fichier déplacer dans {DOCUMENT_DIR}"
                    )
                else:
                    raise FolderInitializationError(DOCUMENT_DIR)
            elif selected_option == 2:
                self.open_file_explorer_and_prompt(file_path)
                root.destroy()
                messagebox.showinfo(
                    "Succès", f"Ouverture de l'explorateur de fichier réussie"
                )
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de récupération de la séléction pour la fenêtre de document: {e}")
        root.quit()

    """ fonction : prompt_user_for_action
        description : Demander a l'utilisateur si il veut déplacer le fichier image dans le dossier wallpaper,
            le dossier image
            ou si il veut le faire manuellement
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download
        sortie : NULL
    """

    def prompt_user_for_action(self, file_path):
        try:
            root = tk.Tk()
            root.withdraw()

            option = tk.IntVar()
            top = tk.Toplevel(root)
            top.title("Choisir une option")
            tk.Label(top, text="Ou voulez vous Déplacer le fichier?").pack(anchor=tk.W)
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
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de création de la fenêtre d'image: {e}")

        try:
            selected_option = option.get()

            # Si option 1 on déplace le fichier dans le dossier wallpaper
            if selected_option == 1:
                if self.folder_init(WALLPAPER_DIR):
                    # Fonction qui déplace le fichier dans le dossier de destination ici wallpaper
                    self.move_file(file_path, WALLPAPER_DIR)
                    root.destroy()
                    # Message de comfirmation de la réussite du programme
                    messagebox.showinfo(
                        "Succès", f"Fichier déplacer dans {WALLPAPER_DIR}"
                    )
                else:
                    raise FolderInitializationError(WALLPAPER_DIR)
            # Si option 2 on déplace le fichier dans le dossier image
            elif selected_option == 2:
                if self.folder_init(IMAGES_DIR):
                    # Fonction qui déplace le fichier dans le dossier de destination ici image
                    self.move_file(file_path, IMAGES_DIR)
                    root.destroy()
                    messagebox.showinfo(
                        "Succès", f"Fichier déplacer dans {IMAGES_DIR}"
                    )
                else:
                    raise FolderInitializationError(IMAGES_DIR)
            elif selected_option == 3:
                self.open_file_explorer_and_prompt(file_path)
                root.destroy()
                messagebox.showinfo(
                    "Succès", f"Ouverture de l'explorateur de fichier réussie"
                )
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de récupération de la séléction pour la fenêtre d'image: {e}")

        root.quit()

    """ fonction : move_file
        description : Déplacer un fichier contenu dans file_path vers le dossier de destination contenu dans destination_dir
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download,
            destination_dir : Chemin du dossier de destination
        sortie : NULL
    """

    def move_file(self, file_path, destination_dir):
        try:
            # Récupération du nom du fichier
            file_name = os.path.basename(file_path)
            # Nouveau chemin créer a partir du nom de fichier et le dossier de destination
            new_path = os.path.join(destination_dir, file_name)
            # Déplacer le fichier dans le nouveau chemin
            shutil.move(file_path, new_path)
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec du déplacement de fichier: {e}")

    """ fonction : move_file_create_dir
        description : Déplacer un fichier contenu dans file_path dans un sous dossier portant le meme nom que le fichier
            dans le dossier de destination contenu dans destination_dir
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download,
            destination_dir : Chemin du dossier de destination
        sortie : NULL
    """

    def move_file_create_dir(self, file_path, destination_dir):
        try:
            file_name = os.path.basename(file_path)

            # Récupération du nom du fichier sans l'extension
            file_name_without_ext = os.path.splitext(file_name)[0]

            # Nouveau chemin créer a partir du nom de fichier sans extension et du dossier de destination
            new_dir_path = os.path.join(destination_dir, file_name_without_ext)
            
            # Création du sous dossier dans le dossier de destination ayant le nom du fichier sans extension
            os.makedirs(new_dir_path, exist_ok=True)

            # Nouveau chemin créer a partir du nom de fichier et le dossier de destination
            new_file_path = os.path.join(new_dir_path, file_name)

            # Déplacer le fichier dans le nouveau chemin
            shutil.move(file_path, new_file_path)
        # Gestion d'erreur de la fonction
        except Exception as e:
                messagebox.showerror("Erreur", f"Échec du déplacement de fichier: {e}")

    """ fonction : move_file_project
        description : Déplacer un fichier contenu dans file_path vers un sous dossier contenu dans une liste des dossier
            dans le dossier de destination contenu dans destination_dir 
        paramètres : file_path : Nom complet du fichier trouvé dans le dossier download,
            destination_dir : Chemin du dossier de destination
        sortie : NULL
    """

    def move_file_project(self, file_path, destination_dir):

        # Récupérer une liste de tous les sous dossier contenu dans le dossier de destination
        dirs = [
            d
            for d in os.listdir(destination_dir)
            if os.path.isdir(os.path.join(destination_dir, d))
        ]

        # Message d'erreur si aucun dossier n'a été trouvé
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

        # Si le dossier choisi est dans la liste de dossier déplacer le fichier dans le sous dossier
        if selected_dir in dirs:
            # Déplace le fichier dans le dossier séléctionner
            destination_path = os.path.join(
                destination_dir, selected_dir, os.path.basename(file_path)
            )
            try:
                shutil.move(file_path, destination_path)
                messagebox.showinfo(
                    "Succès", f"Fichier déplacer dans {destination_path}"
                )
            except Exception as e:
                messagebox.showerror("Erreur", f"Échec du déplacement de fichier: {e}")
        else:
            messagebox.showerror("Erreur", "Dossier invalide ou séléction annuler.")

        # Destruction de la fenetre pour éviter les bug quand on relance une fenetre
        root.destroy()

    """ fonction : open_file_explorer_and_prompt
        description : ouvrir l'explorateur du fichier a l'endroit ou se trouve le fichier
        paramètres : file_path : nom complet du fichier trouvé dans le dossier download,
        sortie : aucun
    """

    def open_file_explorer_and_prompt(self, file_path):
        try:
            # Ouverture du dossier dans l'explorateur du fichier a l'endroit ou se trouve le fichier
            file_dir = os.path.dirname(file_path)
            if os.name == "nt":  # Windows
                subprocess.Popen(f'explorer /select,"{file_path}"')
        except Exception as e:
                messagebox.showerror("Erreur", f"Échec du déplacement de fichier: {e}")
