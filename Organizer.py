import time
from watchdog.observers import Observer
from OrganizerHandler import OrganizerHandler

if __name__ == "__main__":
    donwloadPath = r"CheminVersLeDossierTéléchargement"
    # Lancement du handler qui gére l'évenement déclencher par watchdog
    event_handler = OrganizerHandler()
    # Dans le main thread on ajoute un observer watchdog qui détécte si un fichier est détécter dans le dossier download
    observer = Observer()
    # Mise en place de l'observer watchdog
    observer.schedule(event_handler, donwloadPath, recursive=False)
    # Lancement de l'observer
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
