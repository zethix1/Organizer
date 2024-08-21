import time
from watchdog.observers import Observer
from OrganizerHandler import OrganizerHandler

if __name__ == "__main__":
    donwloadPath = r"C:\Users\dksll\Downloads"
    # lancement du handler qui gére l'évenement déclencher par watchdog
    event_handler = OrganizerHandler()
    # dans le main thread on ajoute un observer watchdog qui détécte si un fichier est détécter dans le dossier download
    observer = Observer()
    # mise en place de l'observer watchdog
    observer.schedule(event_handler, donwloadPath, recursive=False)
    # lancement de l'observer
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
