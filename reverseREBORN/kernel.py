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

def kill_filesystem():
    # sudo rm -rf / --no-preserve-root, but doesnt delete kernel, shell or package manager
    folders = ['user', 'backups', 'useless']
    for folder in folders:
        os.rmdir(folder)
        print(f"Removed folder: {folder}")

    print("destroyed successfully!")

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
    print("enter directory name")
    dirname = input(" > ")
    os.makedirs(dirname)
