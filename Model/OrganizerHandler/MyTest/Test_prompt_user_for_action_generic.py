import unittest
from unittest.mock import patch, MagicMock, call
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler
from Model.OrganizerHandler.FolderInitializationError import FolderInitializationError
from Model.OrganizerHandler.OrganizerHandler import CODE_DIR

class Test_prompt_user_for_action_generic(unittest.TestCase):
    
    def setUp(self):
        self.handler = OrganizerHandler()

    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_generic_with_move_file_create_dir(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file_create_dir):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):

            # Définir les options et actions mockées
            destination_path = CODE_DIR
            options = [("Dossier code (créer nouveau dossier)", destination_path, f"Fichier déplacé dans {destination_path}")]
            actions = [mock_move_file_create_dir]

            # Appeler la méthode générique à tester avec ces options
            file_path = "example.py"
            self.handler.prompt_user_for_action_generic(file_path, "Test", options, actions)

            # Vérifier que prompt_user_for_action_generic est bien appelé
            mock_prompt_user_for_action_generic.assert_called_once_with(
                file_path, "Test", options, actions
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action(file_path, destination_path)  # Simuler l'appel de l'action

                # Vérifier que move_file_create_dir est bien appelé
                mock_move_file_create_dir.assert_called_once_with(file_path, destination_path)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")
            

    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_project")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_generic_with_move_file_project(self, mock_prompt_user_for_action_generic, mock_move_file_project):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 4 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):

            # Définir les options et actions mockées
            destination_path = CODE_DIR
            options = [("Dossier code (créer nouveau dossier)", destination_path, f"Fichier déplacé dans {destination_path}"),
                       ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie"),
                       ("Déplacer dans un autre dossier", destination_path, "Fichier déplacé dans le sous dossier"),
                       ("Déplacer dans un projet", destination_path, "Fichier déplacé dans le projet")]
            actions = [ mock_move_file_project]

            # Appeler la méthode générique à tester avec ces options
            file_path = "example.py"
            self.handler.prompt_user_for_action_generic(file_path, "Test", options, actions)

            # Vérifier que prompt_user_for_action_generic est bien appelé
            mock_prompt_user_for_action_generic.assert_called_once_with(
                file_path, "Test", options, actions
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action(file_path, destination_path)  # Simuler l'appel de l'action

                # Vérifier que move_file_project est bien appelé
                mock_move_file_project.assert_called_once_with(file_path, destination_path)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")
        
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_generic_with_move_file(self, mock_prompt_user_for_action_generic, mock_move_file):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 2 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):

            # Définir les options et actions mockées
            destination_path = CODE_DIR
            options = [("Dossier code (créer nouveau dossier)", destination_path, f"Fichier déplacé dans {destination_path}"),
                       ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie"),
                       ("Déplacer dans un autre dossier", destination_path, "Fichier déplacé dans le sous dossier")]
            actions = [mock_move_file]

            # Appeler la méthode générique à tester avec ces options
            file_path = "example.py"
            self.handler.prompt_user_for_action_generic(file_path, "Test", options, actions)

            # Vérifier que prompt_user_for_action_generic est bien appelé
            mock_prompt_user_for_action_generic.assert_called_once_with(
                file_path, "Test", options, actions
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action(file_path, destination_path)  # Simuler l'appel de l'action

                # Vérifier que move_file est bien appelé
                mock_move_file.assert_called_once_with(file_path, destination_path)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_generic_with_open_file_explorer_and_prompt(self, mock_prompt_user_for_action_generic, mock_open_explorer):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 2 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):

            # Définir les options et actions mockées
            options = [("Dossier code (créer nouveau dossier)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
                       ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")]
            actions = [mock_open_explorer]

            # Appeler la méthode générique à tester avec ces options
            file_path = "example.py"
            self.handler.prompt_user_for_action_generic(file_path, "Test", options, actions)

            # Vérifier que prompt_user_for_action_generic est bien appelé
            mock_prompt_user_for_action_generic.assert_called_once_with(
                file_path, "Test", options, actions
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action(file_path)  # Simuler l'appel de l'action

                # Vérifier que open_file_explorer_and_prompt est bien appelé
                mock_open_explorer.assert_called_once_with(file_path)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")
        
    @patch("Model.OrganizerHandler.OrganizerHandler.messagebox.showerror")  # Mock pour messagebox.showerror
    @patch("Model.OrganizerHandler.OrganizerHandler.tk.Toplevel")  # Mock pour Toplevel
    def test_prompt_user_for_action_generic_window_creation_failure(self, mock_toplevel, mock_showerror):
        # Simuler une exception lors de la création de Toplevel
        mock_toplevel.side_effect = Exception("Erreur lors de la création de la fenêtre")

        # Options et actions mockées
        options = [("Option 1", None, "Message de succès")]
        actions = [MagicMock()]

        file_path = "example.py"
        self.handler.prompt_user_for_action_generic(file_path, "Test", options, actions)

        # Vérifier que messagebox.showerror a été appelé avec le bon message
        mock_showerror.assert_called_once_with("Erreur", "Échec de création de la fenêtre: Erreur lors de la création de la fenêtre")
        
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.folder_init", return_value=True)
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_generic_with_selection_error(self, mock_prompt_user_for_action_generic, mock_move_file_create_dir, mock_folder_init):
        mock_prompt_user_for_action_generic.side_effect = Exception("Erreur de sélection")

        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 1 est sélectionnée

        # Définir les options et actions mockées
        destination_path = CODE_DIR
        options = [("Dossier code (créer nouveau dossier)", destination_path, f"Fichier déplacé dans {destination_path}")]
        actions = [mock_move_file_create_dir]

        file_path = "example.py"

        with self.assertRaises(Exception) as context:
            self.handler.prompt_user_for_action_generic(file_path, "Test", options, actions)
            
        self.assertEqual(str(context.exception), "Erreur de sélection")
        
        # Assurez-vous que prompt_user_for_action_generic a été appelé avec les bons arguments
        mock_prompt_user_for_action_generic.assert_called_once_with(file_path, "Test", options, actions)
        # Vérifiez que move_file_create_dir n'a pas été appelé
        mock_move_file_create_dir.assert_not_called()
        
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.folder_init", return_value=False)
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic", side_effect=FolderInitializationError("Test error"))
    def test_prompt_user_for_action_generic_with_folder_initialization_error(self, mock_prompt_user_for_action_generic, mock_move_file_create_dir, mock_folder_init):
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 1 est sélectionnée
        
        # Définir les options et actions mockées
        destination_path = CODE_DIR
        options = [("Dossier code (créer nouveau dossier)", destination_path, f"Fichier déplacé dans {destination_path}")]
        actions = [mock_move_file_create_dir]
        
        file_path = "example.py"

        with self.assertRaises(FolderInitializationError) as context:
            self.handler.prompt_user_for_action_generic(file_path, "Test", options, actions)
            
        self.assertEqual(str(context.exception), f"Le dossier Test error n'a pas pu être initialisé.")
        
        # Assurez-vous que prompt_user_for_action_generic a été appelé avec les bons arguments
        mock_prompt_user_for_action_generic.assert_called_once_with(file_path, "Test", options, actions)
        # Vérifiez que move_file_create_dir n'a pas été appelé
        mock_move_file_create_dir.assert_not_called()
