import unittest
from unittest.mock import patch, MagicMock, call
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler

class Test_is_something(unittest.TestCase):
    
    def setUp(self):
        self.handler = OrganizerHandler()
        
    @patch("Model.OrganizerHandler.OrganizerHandler.messagebox.showerror")
    def test_is_image(self, mock_showerror):
        # Test cases for different file extensions
        self.assertTrue(self.handler.is_image("example.jpg"))
        self.assertTrue(self.handler.is_image("example.PNG"))
        self.assertFalse(self.handler.is_image("example.txt"))
        
        # Test error handling
        with patch("Model.OrganizerHandler.OrganizerHandler.os.path.splitext", side_effect=Exception("Test error")):
            self.assertFalse(self.handler.is_image("example.jpg"))
            mock_showerror.assert_called_once_with("Erreur", "Échec de séparation du nom de fichier: Test error")
    
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_image", side_effect=Exception("Test error"))
    def test_is_image_with_exception(self, mock_is_image):
        
        with self.assertRaises(Exception) as context:
            self.handler.is_image("example.jpg")
            
        # Vérifiez que l'exception a le message attendu
        self.assertEqual(str(context.exception), "Test error")

        # Vérifiez que la méthode patchée (is_zip) a été appelée
        mock_is_image.assert_called_once_with("example.jpg")

    @patch("Model.OrganizerHandler.OrganizerHandler.messagebox.showerror")
    def test_is_doc(self, mock_showerror):
        self.assertTrue(self.handler.is_doc("example.pdf"))
        self.assertTrue(self.handler.is_doc("example.DOCX"))
        self.assertFalse(self.handler.is_doc("example.zip"))

        with patch("Model.OrganizerHandler.OrganizerHandler.os.path.splitext", side_effect=Exception("Test error")):
            self.assertFalse(self.handler.is_doc("example.pdf"))
            mock_showerror.assert_called_once_with("Erreur", "Échec de séparation du nom de fichier: Test error")
    
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_doc", side_effect=Exception("Test error"))
    def test_is_doc_with_exception(self, mock_is_doc):
        
        with self.assertRaises(Exception) as context:
            self.handler.is_doc("example.docx")
            
        # Vérifiez que l'exception a le message attendu
        self.assertEqual(str(context.exception), "Test error")

        # Vérifiez que la méthode patchée (is_zip) a été appelée
        mock_is_doc.assert_called_once_with("example.docx")

    @patch("Model.OrganizerHandler.OrganizerHandler.messagebox.showerror")
    def test_is_code(self, mock_showerror):
        self.assertTrue(self.handler.is_code("example.py"))
        self.assertTrue(self.handler.is_code("example.JAVA"))
        self.assertFalse(self.handler.is_code("example.docx"))

        with patch("Model.OrganizerHandler.OrganizerHandler.os.path.splitext", side_effect=Exception("Test error")):
            self.assertFalse(self.handler.is_code("example.py"))
            mock_showerror.assert_called_once_with("Erreur", "Échec de séparation du nom de fichier: Test error")
    
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_code", side_effect=Exception("Test error"))
    def test_is_code_with_exception(self, mock_is_code):
        
        with self.assertRaises(Exception) as context:
            self.handler.is_code("example.py")
            
        # Vérifiez que l'exception a le message attendu
        self.assertEqual(str(context.exception), "Test error")

        # Vérifiez que la méthode patchée (is_zip) a été appelée
        mock_is_code.assert_called_once_with("example.py")

    @patch("Model.OrganizerHandler.OrganizerHandler.messagebox.showerror")
    def test_is_zip(self, mock_showerror):
        self.assertTrue(self.handler.is_zip("example.zip"))
        self.assertTrue(self.handler.is_zip("example.7z"))
        self.assertTrue(self.handler.is_zip("example.tar.gz"))
        self.assertFalse(self.handler.is_zip("example.docx"))
            
    @patch("Model.OrganizerHandler.OrganizerHandler.OrganizerHandler.is_zip", side_effect=Exception("Test error"))
    def test_is_zip_with_exception(self, mock_is_zip):
        
        with self.assertRaises(Exception) as context:
            self.handler.is_zip("example.zip")
            
        # Vérifiez que l'exception a le message attendu
        self.assertEqual(str(context.exception), "Test error")

        # Vérifiez que la méthode patchée (is_zip) a été appelée
        mock_is_zip.assert_called_once_with("example.zip")