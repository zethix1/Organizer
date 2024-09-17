from watchdog.events import FileSystemEventHandler
import os
import tkinter as tk
import shutil
import subprocess
from tkinter import messagebox
from tkinter import simpledialog
from pathlib import Path
from Model.OrganizerHandler.FolderInitializationError import FolderInitializationError

# Récupération des deux chemins principaux(image et document) dynamiquement
pictures_dir = Path.home() / "Pictures"
documents_dir = Path.home() / "Documents"

# Chemin dynamique des différents dossier wallpaper, image, document, code et zip
WALLPAPER_DIR = pictures_dir / "wallpaper"
IMAGES_DIR = pictures_dir
DOCUMENT_DIR = documents_dir
CODE_DIR = documents_dir / "Code"
ZIP_DIR = documents_dir / "Zip"

class OrganizerHandler(FileSystemEventHandler):
    """Class qui a pour but de gérer l'ajout d'un fichier dans le dossier download détécté par le watchdog que se soit un fichier image, code, document ou zip

    Args:
        FileSystemEventHandler : Événement déclenché par le watchdog

    Raises:
        FolderInitializationError: Exception levée lorsqu'un dossier ne peut pas être initialisé

    """    
    
    def on_created(self, event):
        """Vérifie quel fonction activer en fonction du fichier récupérer par l'évenement watchdog

        Args:
            event: Événement déclenché par le watchdog
        """        
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
        """Vérifie si le dossier existe, sinon le crée

        Args:
            folder_path (Path) : Chemin du dossier a vérifier

        Returns:
            bool: Vraie si le dossier existe ou a été initialisé sinon retourne faux si le dossier n'existe pas et n'a pas pu etre initialisé
        """        
        try:
            # Vérifie si le dossier existe et le crée si il n'existe pas
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
            return True
        except Exception:
            return False

    def is_image(self, file_path):
        """Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier image

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download

        Returns:
            bool: Vraie si fichier est image faux si fichier n'est pas image
        """        
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

    def is_doc(self, file_path):
        """Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier zip

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download

        Returns:
            bool: Vraie si fichier est zip faux si fichier n'est pas zip
        """        
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

    def is_code(self, file_path):
        """Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier code

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download

        Returns:
            bool: Vraie si fichier est code faux si fichier n'est pas code
        """        
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

    def is_zip(self, file_path):
        """Vérifie si le fichier récupérer dans le dossier download contenu dans file_path est un fichier zip

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download

        Returns:
            bool: Vraie si fichier est zip faux si fichier n'est pas zip
        """        
        # Liste d'extension de zip
        zip_extensions = {
            ".zip",
            ".7z",
            ".tar.gz",
            ".rar"
        }
        try:
            for ext in zip_extensions:
                if file_path.endswith(ext):
                    return True
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de séparation du nom de fichier: {e}")
        return False
    
    def prompt_user_for_action_generic(self, file_path, title, options, actions):
        """Demander à l'utilisateur de choisir une option pour déplacer un fichier.

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download.
            title : Titre de la fenêtre de sélection.
            options : Liste de tuples contenant les options et les actions correspondantes.
                    Chaque tuple a la forme (texte_option, dossier_destination, message_succès).
            actions : Liste de fonctions à appeler pour chaque option. 
                    La fonction doit accepter file_path et un dossier en argument.

        Raises:
            FolderInitializationError : Exception levée lorsqu'un dossier ne peut pas être initialisé
            Exception(sélection) : Lorsque la séléction de la fenêtre échoue une exception est levé
            Exception(création de la fenêtre) : Lorsque la création de la fenêtre échoue une exception est levé
        """
        try:
            root = tk.Tk()
            root.withdraw()

            option_var = tk.IntVar()
            top = tk.Toplevel(root)
            top.title(title)
            tk.Label(top, text="Où voulez-vous déplacer le fichier?").pack(anchor=tk.W)

            # Créer des boutons radio pour chaque option
            for idx, (text_option, _, _) in enumerate(options, start=1):
                tk.Radiobutton(top, text=text_option, variable=option_var, value=idx).pack(anchor=tk.W)

            tk.Button(top, text="OK", command=top.quit).pack()

            def on_close():
                root.destroy()

            top.protocol("WM_DELETE_WINDOW", on_close)
            root.eval(f"tk::PlaceWindow {str(top)} center")
            top.geometry("300x140")
            top.wm_attributes("-topmost", True)

            top.mainloop()
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec de création de la fenêtre: {e}")
            return

        # Simuler la sélection de l'option pendant les tests
        try:
            selected_option = option_var.get()
            if 1 <= selected_option <= len(options):
                text_option, target_dir, success_message = options[selected_option - 1]
                action = actions[selected_option - 1]

                if target_dir:  # Si target_dir n'est pas None, on effectue l'action
                    if self.folder_init(target_dir):
                        root.destroy()
                        action(file_path, target_dir)
                        messagebox.showinfo("Succès", success_message)
                    else:
                        raise FolderInitializationError(target_dir)
                else:  # Si target_dir est None, on effectue l'action manuelle
                    action(file_path)
                    root.destroy()
                    messagebox.showinfo("Succès", "Ouverture de l'explorateur de fichier réussie")
        except Exception as e:
            print(f"Exception capturée: {e}")  # Débogage
            messagebox.showerror("Erreur", f"Échec de récupération de la sélection: {e}")
        finally:
            root.quit()
            
    def prompt_user_for_action_zip(self, file_path):
        """Demander a l'utilisateur si il veut déplacer le fichier zip dans un sous dossier du nom du fichier dans le dossier zip, si il veut le déplacer le fichier dans un sous dossier du dossier zip déjà existant ou si il veut le faire manuellement

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
        """        
        options = [
            ("Dossier zip (créer nouveau dossier)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
            ("Dossier zip (mettre dans un dossier existant)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
            ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie"),
        ]
        actions = [
            self.move_file_create_dir,
            self.move_file_project,
            self.open_file_explorer_and_prompt
        ]
        self.prompt_user_for_action_generic(file_path, "Choisir une option", options, actions)


    def prompt_user_for_action_code(self, file_path):
        """Demander a l'utilisateur si il veut déplacer le fichier code dans un sous dossier du nom du fichier dans le dossier code, si il veut déplacer le fichier dans un sous dossier du dossier code déjà existant ou si il veut le faire manuellement

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
        """
        options = [
            ("Dossier code (créer nouveau dossier)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
            ("Dossier code (mettre dans un dossier existant)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
            ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie"),
        ]
        actions = [
            self.move_file_create_dir,
            self.move_file_project,
            self.open_file_explorer_and_prompt
        ]
        self.prompt_user_for_action_generic(file_path, "Choisir une option", options, actions)
        
    def prompt_user_for_action_doc(self, file_path):
        """Demander a l'utilisateur si il veut déplacer le fichier document dans le dossier document ou si il veut le faire manuellement

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
        """
        options = [
            ("Dossier documents (créer un nouveau dossier)", DOCUMENT_DIR, f"Fichier déplacé dans {DOCUMENT_DIR}"),
            ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie"),
        ]
        actions = [
            self.move_file_create_dir,
            self.open_file_explorer_and_prompt
        ]
        
        self.prompt_user_for_action_generic(file_path, "Choisir une option", options, actions)
        
    def prompt_user_for_action(self, file_path):
        """Demander a l'utilisateur si il veut déplacer le fichier image dans le dossier wallpaper, le dossier image ou si il veut le faire manuellement

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
        """
        options = [
            ("Dossier wallpaper", WALLPAPER_DIR, f"Fichier déplacé dans {WALLPAPER_DIR}"),
            ("Dossier images", IMAGES_DIR, f"Fichier déplacé dans {IMAGES_DIR}"),
            ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie"),
        ]
        actions = [
            self.move_file,
            self.move_file,
            self.open_file_explorer_and_prompt
        ]
        self.prompt_user_for_action_generic(file_path, "Choisir une option", options, actions)

    def move_file(self, file_path, destination_dir):
        """Déplacer un fichier contenu dans file_path vers le dossier de destination contenu dans destination_dir

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
            destination_dir : Chemin du dossier de destination
        """        
        try:
            # Récupération du nom du fichier
            file_name = os.path.basename(file_path)
            file_path = os.path.normpath(file_path)
            # Nouveau chemin créer a partir du nom de fichier et le dossier de destination
            new_path = os.path.join(destination_dir, file_name)
            new_path = os.path.normpath(new_path)
            # Déplacer le fichier dans le nouveau chemin
            shutil.move(file_path, new_path)
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec du déplacement de fichier: {e}")

    def move_file_create_dir(self, file_path, destination_dir):
        """Déplacer un fichier contenu dans file_path dans un sous dossier portant le meme nom que le fichier dans le dossier de destination contenu dans destination_dir

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
            destination_dir : Chemin du dossier de destination
        """        
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

    def move_file_project(self, file_path, destination_dir):
        """Déplacer un fichier contenu dans file_path vers un sous dossier contenu dans une liste des dossier dans le dossier de destination contenu dans destination_dir

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
            destination_dir : Chemin du dossier de destination
        """        

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

    def open_file_explorer_and_prompt(self, file_path):
        """Ouvrir l'explorateur du fichier a l'endroit ou se trouve le fichier

        Args:
            file_path : Nom complet du fichier trouvé dans le dossier download
        """        
        try:
            # Ouverture du dossier dans l'explorateur du fichier a l'endroit ou se trouve le fichier
            file_dir = os.path.dirname(file_path)
            if os.name == "nt":  # Windows
                subprocess.Popen(f'explorer /select,"{file_path}"')
        except Exception as e:
                messagebox.showerror("Erreur", f"Échec du déplacement de fichier: {e}")
