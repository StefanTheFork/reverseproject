import os
import shutil
from datetime import datetime
time = datetime.now()

# scans if you got unix/linux or windows
if os.name == 'posix':
    clear = "clear"
elif os.name == 'nt':
    clear = "cls"
else:
    print('\n' * 100)


# basic kernel stuff

dirname = ""

def onboot():
    print("Started!")
    print("Hello, World!")
    # example onboot entry. put kernel.onboot() in your shell file as a standalone line and you can execute stuff like a logo or clock thing.

def setup_filesystem():
    # creates beautiful file system
    folders = ['user', 'backups', 'useless']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"maked {folder}")

    print("file system is ready!")

def kill_filesystem():
    # sudo rm -rf / --no-preserve-root, but doesnt delete kernel, shell or package manager
    folders = ['user', 'backups', 'useless']
    for folder in folders:
        shutil.rmtree(folder)
        print(f"got rid of {folder}")

    print("destroyed successfully!")


def clear_screen():
    # hmmmmmm i wonder what it does
    os.system(clear)

def clock():
    # GUESS WHAT! ITS A CLOCK!
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

def createdir():
    # can you guess what it does?
    os.makedirs(dirname)
