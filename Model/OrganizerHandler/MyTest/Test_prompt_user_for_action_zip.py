import unittest
from unittest.mock import patch, MagicMock, call
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler
from Model.OrganizerHandler.FolderInitializationError import FolderInitializationError
from Model.OrganizerHandler.OrganizerHandler import ZIP_DIR

class Test_prompt_user_for_action_zip(unittest.TestCase):
    
    def setUp(self):
        self.handler = OrganizerHandler()
        
    # faire test option 1 et 2 sur le modéle de code et doc
    
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_project")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_zip_option1(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file_project, mock_move_file_create_dir):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action_zip("example.zip")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.zip", "Choisir une option", 
                [("Dossier zip (créer nouveau dossier)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
                ("Dossier zip (mettre dans un dossier existant)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file_create_dir, mock_move_file_project, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.zip", ZIP_DIR)  # Simuler l'appel de l'action
                
                # Vérifier que move_file_create_dir est bien appelé pour l'option 1
                mock_move_file_create_dir.assert_called_once_with("example.zip", ZIP_DIR)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que move_file_project et open_file_explorer_and_prompt ne sont pas appelés
            assert not mock_move_file_project.called, "move_file_project should not have been called"
            assert not mock_open_explorer.called, "open_file_explorer_and_prompt should not have been called"
            
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_project")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_zip_option2(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file_project, mock_move_file_create_dir):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 2  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action_zip("example.zip")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.zip", "Choisir une option", 
                [("Dossier zip (créer nouveau dossier)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
                ("Dossier zip (mettre dans un dossier existant)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file_create_dir, mock_move_file_project, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.zip", ZIP_DIR)  # Simuler l'appel de l'action
                
                # Vérifier que move_file_create_dir est bien appelé pour l'option 1
                mock_move_file_project.assert_called_once_with("example.zip", ZIP_DIR)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que move_file_project et open_file_explorer_and_prompt ne sont pas appelés
            assert not mock_move_file_create_dir.called, "move_file_create_dir should not have been called"
            assert not mock_open_explorer.called, "open_file_explorer_and_prompt should not have been called"
            
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_project")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_zip_option3(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file_project, mock_move_file_create_dir):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 3  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action_zip("example.zip")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.zip", "Choisir une option", 
                [("Dossier zip (créer nouveau dossier)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
                ("Dossier zip (mettre dans un dossier existant)", ZIP_DIR, f"Fichier déplacé dans {ZIP_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file_create_dir, mock_move_file_project, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.zip")  # Simuler l'appel de l'action
                
                # Vérifier que move_file_create_dir est bien appelé pour l'option 1
                mock_open_explorer.assert_called_once_with("example.zip")
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que move_file_project et open_file_explorer_and_prompt ne sont pas appelés
            assert not mock_move_file_project.called, "move_file_project should not have been called"
            assert not mock_move_file_create_dir.called, "move_file_create_dir should not have been called"