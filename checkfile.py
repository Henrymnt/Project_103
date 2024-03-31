import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/Henry/Downloads"
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       print(f"{event.src_path} has been created.")
    def on_modified(self, event):
       print(f"{event.src_path} has been modified.")       
    def on_moved(self, event):
       print(f"{event.src_path} has been moved.")
    def on_deleated(self, event):
       print(f"{event.src_path} has been deleted.")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Program stopped!")
    observer.stop()
