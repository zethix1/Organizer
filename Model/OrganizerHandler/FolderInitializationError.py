class FolderInitializationError(Exception):
    """Exception levée lorsqu'un dossier ne peut pas être initialisé

    Args:
        Exception : class d'exception
    """    
    def __init__(self, folder_path):
        """Initialisation de la class

        Args:
            folder_path : chemin du dossier ayant produit l'exception
        """        
        super().__init__(f"Le dossier {folder_path} n'a pas pu être initialisé.")
        self.folder_path = folder_path
