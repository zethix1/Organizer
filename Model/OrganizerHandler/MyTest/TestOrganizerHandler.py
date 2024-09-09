import unittest
from unittest.mock import patch, MagicMock, call
from pathlib import Path
from Model.OrganizerHandler.OrganizerHandler import OrganizerHandler, FolderInitializationError
from Model.OrganizerHandler.OrganizerHandler import CODE_DIR,WALLPAPER_DIR,IMAGES_DIR,DOCUMENT_DIR,ZIP_DIR



class TestOrganizerHandler(unittest.TestCase):
    
    def setUp(self):
        # Instantiate the OrganizerHandler for use in tests
        self.handler = OrganizerHandler()





if __name__ == "__main__":
    unittest.main()
