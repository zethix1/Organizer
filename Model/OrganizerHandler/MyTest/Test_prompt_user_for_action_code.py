import unittest
from unittest.mock import patch, MagicMock, call
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler
from Model.OrganizerHandler.FolderInitializationError import FolderInitializationError
from Model.OrganizerHandler.OrganizerHandler import CODE_DIR

class Test_prompt_user_for_action_code(unittest.TestCase):
    
    def setUp(self):
        self.handler = OrganizerHandler()

    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_project")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_code_option1(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file_project, mock_move_file_create_dir):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 1  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action_code("example.py")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.py", "Choisir une option", 
                [("Dossier code (créer nouveau dossier)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
                ("Dossier code (mettre dans un dossier existant)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file_create_dir, mock_move_file_project, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.py", CODE_DIR)  # Simuler l'appel de l'action
                
                # Vérifier que move_file_create_dir est bien appelé pour l'option 1
                mock_move_file_create_dir.assert_called_once_with("example.py", CODE_DIR)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que move_file_project et open_file_explorer_and_prompt ne sont pas appelés
            assert not mock_move_file_project.called, "move_file_project should not have been called"
            assert not mock_open_explorer.called, "open_file_explorer_and_prompt should not have been called"

            
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_project")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_code_option2(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file_project, mock_move_file_create_dir):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 2  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action_code("example.py")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.py", "Choisir une option", 
                [("Dossier code (créer nouveau dossier)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
                ("Dossier code (mettre dans un dossier existant)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file_create_dir, mock_move_file_project, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.py", CODE_DIR)  # Simuler l'appel de l'action
                
                # Vérifier que move_file_create_dir est bien appelé pour l'option 1
                mock_move_file_project.assert_called_once_with("example.py", CODE_DIR)
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que move_file_project et open_file_explorer_and_prompt ne sont pas appelés
            assert not mock_move_file_create_dir.called, "move_file_create_dir should not have been called"
            assert not mock_open_explorer.called, "open_file_explorer_and_prompt should not have been called"
            
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_create_dir")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.move_file_project")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.open_file_explorer_and_prompt")
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.prompt_user_for_action_generic")
    def test_prompt_user_for_action_code_option3(self, mock_prompt_user_for_action_generic, mock_open_explorer, mock_move_file_project, mock_move_file_create_dir):
        # Configuration des mocks
        mock_option = MagicMock()
        mock_option.get.return_value = 3  # Simule que l'option 1 est sélectionnée

        with patch("Model.OrganizerHandler.OrganizerHandler.tk.IntVar", return_value=mock_option):
            
            # Appel de la fonction à tester
            self.handler.prompt_user_for_action_code("example.py")

            # Vérifier que prompt_user_for_action_generic est bien appelé avec les bons arguments
            mock_prompt_user_for_action_generic.assert_called_once_with(
                "example.py", "Choisir une option", 
                [("Dossier code (créer nouveau dossier)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
                ("Dossier code (mettre dans un dossier existant)", CODE_DIR, f"Fichier déplacé dans {CODE_DIR}"),
                ("Autre (déplacer manuellement)", None, "Ouverture de l'explorateur de fichier réussie")],
                [mock_move_file_create_dir, mock_move_file_project, mock_open_explorer]
            )

            # Vérifier les appels des actions
            if mock_prompt_user_for_action_generic.called:
                # Extraire l'action sélectionnée
                args, kwargs = mock_prompt_user_for_action_generic.call_args
                selected_action = args[3][mock_option.get.return_value - 1]
                selected_action("example.py")  # Simuler l'appel de l'action
                
                # Vérifier que move_file_create_dir est bien appelé pour l'option 1
                mock_open_explorer.assert_called_once_with("example.py")
            else:
                print("prompt_user_for_action_generic n'a pas été appelé")

            # Vérifier que move_file_project et open_file_explorer_and_prompt ne sont pas appelés
            assert not mock_move_file_project.called, "move_file_project should not have been called"
            assert not mock_move_file_create_dir.called, "move_file_create_dir should not have been called"

if __name__ == '__main__':
    unittest.main()