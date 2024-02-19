import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "c:/Users/DELL/Downloads"
to_dir = "./downloads"


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

def on_created(self, event):
    
        name,extention=os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            if extention in value:
                file_name=os.path.basename(event.src_path)
                path1=from_dir+"/"+file_name
                path2=to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+file_name
                
                if os.path.exists(path2):
                    print("Folder Exist")
                    print("moving"+file_name)
                    shutil.move(path1,path3)
                    
                    time.sleep(1)                
                else:
                    print("MAKEING DIRECTORY")
                    os.makedirs(path2)
                    
                    print("moving"+file_name)
                    shutil.move(path1,path3)
                    
                    time.sleep(1)
                    
                    
event_handler = FileMovementHandler()


observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()


while True:
    time.sleep(2)
    print("running...")

    