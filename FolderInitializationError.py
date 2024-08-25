class FolderInitializationError(Exception):
    """Exception levée lorsque le dossier ne peut pas être initialisé."""
    def __init__(self, folder_path):
        super().__init__(f"Le dossier {folder_path} n'a pas pu être initialisé.")
        self.folder_path = folder_path
