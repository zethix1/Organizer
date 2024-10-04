import unittest
from unittest.mock import patch, MagicMock, call
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler
from pathlib import Path
import os
from Model.OrganizerHandler.FolderInitializationError import FolderInitializationError

class Test_base(unittest.TestCase):
    
    def setUp(self):
        self.handler = OrganizerHandler()
        
    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_image')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action')
    def test_on_created_with_image(self, mock_prompt_user_for_action, mock_is_image, mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.jpg'

        mock_event.is_directory = os.path.isdir(mock_event.src_path)
        # Simule le retour de la méthode is_image pour qu'elle retourne True
        mock_is_image.return_value = True

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_image.assert_called_once_with('/path/to/file.jpg')

        # Vérifie que prompt_user_for_action a bien été appelée car is_image a retourné True
        mock_prompt_user_for_action.assert_called_once_with('/path/to/file.jpg')

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()

    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_image')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action')
    def test_on_created_with_non_image(self,mock_prompt_user_for_action, mock_is_image,mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.tx'
        mock_event.is_directory = os.path.isdir(mock_event.src_path)

        # Simule le retour de la méthode is_image pour qu'elle retourne False
        mock_is_image.return_value = False

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_image.assert_called_once_with('/path/to/file.tx')

        # Vérifie que prompt_user_for_action n'a pas été appelée car is_image a retourné False
        mock_prompt_user_for_action.assert_not_called()

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()
        
    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_doc')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_doc')
    def test_on_created_with_document(self, mock_prompt_user_for_action_doc, mock_is_doc, mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.txt'
        mock_event.is_directory = os.path.isdir(mock_event.src_path)

        # Simule le retour de la méthode is_image pour qu'elle retourne True
        mock_is_doc.return_value = True

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_doc.assert_called_once_with('/path/to/file.txt')

        # Vérifie que prompt_user_for_action a bien été appelée car is_image a retourné True
        mock_prompt_user_for_action_doc.assert_called_once_with('/path/to/file.txt')

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()

    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_doc')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_doc')
    def test_on_created_with_non_document(self,mock_prompt_user_for_action_doc, mock_is_doc,mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.tx'
        mock_event.is_directory = os.path.isdir(mock_event.src_path)

        # Simule le retour de la méthode is_image pour qu'elle retourne False
        mock_is_doc.return_value = False

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_doc.assert_called_once_with('/path/to/file.tx')

        # Vérifie que prompt_user_for_action n'a pas été appelée car is_image a retourné False
        mock_prompt_user_for_action_doc.assert_not_called()

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()
        
    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_code')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_code')
    def test_on_created_with_code(self, mock_prompt_user_for_action_code, mock_is_code, mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.py'
        mock_event.is_directory = os.path.isdir(mock_event.src_path)

        # Simule le retour de la méthode is_image pour qu'elle retourne True
        mock_is_code.return_value = True

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_code.assert_called_once_with('/path/to/file.py')

        # Vérifie que prompt_user_for_action a bien été appelée car is_image a retourné True
        mock_prompt_user_for_action_code.assert_called_once_with('/path/to/file.py')

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()

    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_code')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_code')
    def test_on_created_with_non_code(self,mock_prompt_user_for_action_code, mock_is_code,mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.tx'
        mock_event.is_directory = os.path.isdir(mock_event.src_path)

        # Simule le retour de la méthode is_image pour qu'elle retourne False
        mock_is_code.return_value = False

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_code.assert_called_once_with('/path/to/file.tx')

        # Vérifie que prompt_user_for_action n'a pas été appelée car is_image a retourné False
        mock_prompt_user_for_action_code.assert_not_called()

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()
        
    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_zip')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_zip')
    def test_on_created_with_zip(self, mock_prompt_user_for_action_zip, mock_is_zip, mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.zip'
        mock_event.is_directory = True

        # Simule le retour de la méthode is_image pour qu'elle retourne True
        mock_is_zip.return_value = True

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_zip.assert_called_once_with('/path/to/file.zip')

        # Vérifie que prompt_user_for_action a bien été appelée car is_image a retourné True
        mock_prompt_user_for_action_zip.assert_called_once_with('/path/to/file.zip')

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()

    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_zip')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_zip')
    def test_on_created_with_non_zip(self,mock_prompt_user_for_action_zip, mock_is_zip,mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.tx'
        mock_event.is_directory = True

        # Simule le retour de la méthode is_image pour qu'elle retourne False
        mock_is_zip.return_value = False

        # Appelle la méthode on_created avec l'événement fictif
        self.handler.on_created(mock_event)

        # Vérifie que is_image a bien été appelée une fois avec le bon chemin de fichier
        mock_is_zip.assert_called_once_with('/path/to/file.tx')

        # Vérifie que prompt_user_for_action n'a pas été appelée car is_image a retourné False
        mock_prompt_user_for_action_zip.assert_not_called()

        # Vérifie que showerror n'a pas été appelé car il n'y a pas eu d'erreur
        mock_showerror.assert_not_called()
    
        
    @patch('Model.OrganizerHandler.OrganizerHandler.messagebox.showerror')
    @patch('Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_image')
    def test_on_created_exception_handling(self, mock_is_image, mock_showerror):
        # Crée un événement fictif
        mock_event = MagicMock()
        mock_event.src_path = '/path/to/file.jpg'
        mock_event.is_directory = os.path.isdir(mock_event.src_path)

        # Simule une exception lors de l'appel de is_image
        mock_is_image.side_effect = Exception("Test Exception")

        # Appelle la méthode on_created avec l'événement fictif, cela doit déclencher l'exception
        self.handler.on_created(mock_event)

        # Vérifie que showerror a bien été appelée à cause de l'exception
        mock_showerror.assert_called_once_with("Erreur", "Échec de vérification du fichier: Test Exception")
        
    
    
    @patch("Model.OrganizerHandler.OrganizerHandler.Path.mkdir")
    def test_folder_init(self, mock_mkdir):
        # Test when the folder already exists
        with patch("Model.OrganizerHandler.OrganizerHandler.Path.exists", return_value=True):
            self.assertTrue(self.handler.folder_init(Path("/some/folder")))

        # Test when the folder does not exist but is created successfully
        with patch("Model.OrganizerHandler.OrganizerHandler.Path.exists", return_value=False):
            self.assertTrue(self.handler.folder_init(Path("/some/folder")))
            mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

        # Test when folder creation fails
        with patch("Model.OrganizerHandler.OrganizerHandler.Path.exists", return_value=False):
            mock_mkdir.side_effect = Exception("Cannot create directory")
            self.assertFalse(self.handler.folder_init(Path("/some/folder")))