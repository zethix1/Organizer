import unittest
from unittest.mock import patch, MagicMock, call
from pathlib import Path
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler
import os

class Test_move_file(unittest.TestCase):
    
        def setUp(self):
            self.handler = OrganizerHandler()
            
        @patch("Model.OrganizerHandler.OrganizerHandler.shutil.move")
        @patch("Model.OrganizerHandler.OrganizerHandler.os.path.basename", return_value="example.py")
        def test_move_file_success(self, mock_basename, mock_move):
            # Test successful file move
            self.handler.move_file("source/path/example.py", "dest/path")
            mock_move.assert_called_once_with("source\\path\\example.py", "dest\\path\\example.py")

        @patch("Model.OrganizerHandler.OrganizerHandler.shutil.move", side_effect=Exception("Move error"))
        @patch("Model.OrganizerHandler.OrganizerHandler.os.path.basename", return_value="example.py")
        @patch("Model.OrganizerHandler.OrganizerHandler.messagebox.showerror")
        def test_move_file_failure(self, mock_showerror, mock_basename, mock_move):
            # Test failure in file move
            self.handler.move_file("source/path/example.py", "dest/path")
            mock_showerror.assert_called_once_with("Erreur", "Échec du déplacement de fichier: Move error")
            
        @patch('Model.OrganizerHandler.OrganizerHandler.shutil.move')
        @patch('Model.OrganizerHandler.OrganizerHandler.os.makedirs')
        def test_move_file_create_dir_success(self, mock_makedirs, mock_move):
            # Crée un faux chemin de fichier et un faux dossier de destination
            file_path = os.path.join('path', 'to', 'source', 'file.txt')
            destination_dir = os.path.join('path', 'to', 'destination')

            # Appelle la méthode move_file_create_dir
            self.handler.move_file_create_dir(file_path, destination_dir)
            
            expected_new_dir_path = os.path.join(destination_dir, 'file')
            expected_new_file_path = os.path.join(expected_new_dir_path, 'file.txt')

            # Vérifie que os.makedirs a été appelé avec le bon chemin
            mock_makedirs.assert_called_once_with(expected_new_dir_path, exist_ok=True)

            # Vérifie que shutil.move a été appelé avec les bons arguments
            mock_move.assert_called_once_with(file_path, expected_new_file_path)
            
        @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
        @patch('Model.OrganizerHandler.OrganizerHandler.shutil.move')
        @patch('Model.OrganizerHandler.OrganizerHandler.os.makedirs')
        def test_move_file_create_dir_failure(self, mock_makedirs, mock_move, mock_showerror):
            # Crée un faux chemin de fichier et un faux dossier de destination
            file_path = '/path/to/source/file.txt'
            destination_dir = '/path/to/destination'

            # Simule une exception lors de l'appel de shutil.move
            mock_move.side_effect = Exception("Test Exception")

            # Appelle la méthode move_file_create_dir, cela doit déclencher l'exception
            self.handler.move_file_create_dir(file_path, destination_dir)

            # Vérifie que showerror a bien été appelée à cause de l'exception
            mock_showerror.assert_called_once_with("Erreur", "Échec du déplacement de fichier: Test Exception")
            
        @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showinfo')
        @patch('Model.OrganizerHandler.OrganizerHandler.shutil.move')
        @patch('Model.OrganizerHandler.OrganizerHandler.simpledialog.askstring')
        @patch('Model.OrganizerHandler.OrganizerHandler.os.path.isdir')
        @patch('Model.OrganizerHandler.OrganizerHandler.os.listdir')
        def test_move_file_project_success(self, mock_listdir, mock_isdir, mock_askstring, mock_move, mock_showinfo):
            # Crée un faux chemin de fichier et un faux dossier de destination
            file_path = os.path.join('path', 'to', 'source', 'file.txt')
            destination_dir = os.path.join('path', 'to', 'destination')
            dirs = ['subdir1', 'subdir2']

            # Configure les mocks
            mock_listdir.return_value = dirs
            mock_isdir.side_effect = lambda d: True  # Tous les éléments dans `dirs` sont des dossiers
            mock_askstring.return_value = 'subdir1'

            # Appelle la méthode move_file_project
            self.handler.move_file_project(file_path, destination_dir)

            # Vérifie que shutil.move a été appelé avec les bons arguments
            expected_destination = os.path.join(destination_dir, 'subdir1', 'file.txt')
            mock_move.assert_called_once_with(file_path, expected_destination)

            # Vérifie que le message de succès a été affiché
            mock_showinfo.assert_called_once_with("Succès", f"Fichier déplacer dans {expected_destination}")

        @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
        @patch('Model.OrganizerHandler.OrganizerHandler.shutil.move')
        @patch('Model.OrganizerHandler.OrganizerHandler.simpledialog.askstring')
        @patch('Model.OrganizerHandler.OrganizerHandler.os.path.isdir')
        @patch('Model.OrganizerHandler.OrganizerHandler.os.listdir')
        def test_move_file_project_failure(self, mock_listdir, mock_isdir, mock_askstring, mock_move, mock_showerror):
            # Crée un faux chemin de fichier et un faux dossier de destination
            file_path = os.path.join('path', 'to', 'source', 'file.txt')
            destination_dir = os.path.join('path', 'to', 'destination')
            dirs = ['subdir1', 'subdir2']

            # Configure les mocks
            mock_listdir.return_value = dirs
            mock_isdir.side_effect = lambda d: True  # Tous les éléments dans `dirs` sont des dossiers
            mock_askstring.return_value = 'subdir1'
            
            # Simule une exception lors de l'appel de shutil.move
            mock_move.side_effect = Exception("Simulated Exception")

            # Appelle la méthode move_file_project, cela doit déclencher l'exception
            self.handler.move_file_project(file_path, destination_dir)

            # Vérifie que showerror a bien été appelée à cause de l'exception
            mock_showerror.assert_called_once_with("Erreur", "Échec du déplacement de fichier: Simulated Exception")

        @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
        @patch('Model.OrganizerHandler.OrganizerHandler.os.listdir')
        def test_move_file_project_no_dirs_found(self, mock_listdir, mock_showerror):
            # Crée un faux chemin de fichier et un faux dossier de destination
            file_path = os.path.join('path', 'to', 'source', 'file.txt')
            destination_dir = os.path.join('path', 'to', 'destination')

            # Configure le mock pour retourner une liste vide (pas de sous-dossiers)
            mock_listdir.return_value = []

            # Appelle la méthode move_file_project
            self.handler.move_file_project(file_path, destination_dir)

            # Vérifie que showerror a bien été appelée à cause de l'absence de sous-dossiers
            mock_showerror.assert_called_once_with(
                "Erreur", "Aucun dossier trouvé dans le dossier de destination."
            )
            
        @patch('Model.OrganizerHandler.OrganizerHandler.subprocess.Popen')
        def test_open_file_explorer_and_prompt_success(self, mock_popen):
            # Crée un faux chemin de fichier
            file_path = os.path.join('path', 'to', 'file.txt')

            # Appelle la méthode open_file_explorer_and_prompt
            self.handler.open_file_explorer_and_prompt(file_path)

            # Vérifie que subprocess.Popen a été appelé avec le bon argument
            mock_popen.assert_called_once_with(f'explorer /select,"{file_path}"')

        @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
        @patch('Model.OrganizerHandler.OrganizerHandler.subprocess.Popen')
        def test_open_file_explorer_and_prompt_failure(self, mock_popen, mock_showerror):
            # Crée un faux chemin de fichier
            file_path = os.path.join('path', 'to', 'file.txt')

            # Configure le mock pour lever une exception lors de l'appel de subprocess.Popen
            mock_popen.side_effect = Exception("Test Exception")

            # Appelle la méthode open_file_explorer_and_prompt, cela doit déclencher l'exception
            self.handler.open_file_explorer_and_prompt(file_path)

            # Vérifie que showerror a bien été appelée à cause de l'exception
            mock_showerror.assert_called_once_with("Erreur", "Échec du déplacement de fichier: Test Exception")
            