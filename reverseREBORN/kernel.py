import os
from datetime import datetime
time = datetime.now()

# basic kernel stuff

dirname = ""

def onboot():
    print("hello world")
    # example onboot entry. put kernel.onboot() in your shell file as a standalone line and you can execute stuff like a logo or clock thing.

def setup_filesystem():
    # creates beautiful file system
    folders = ['user', 'backups', 'useless']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    print("file system is ready!")

def clear_screen():
    # scans if you got unix/linux or windows
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('\n' * 100)

def clock():
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

def createdir():
    os.makedirs(dirname)
