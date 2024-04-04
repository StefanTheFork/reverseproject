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
    #removes user backups and useless folder, its for when you want to redo your file structure
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
    current_time = time.strftime("%H:%M:%S")
    print(current_time)

def makefile(filename):
    #DOES THIS MAKE A FILE? I HAVE NO IDEA!
    try:
        with open(filename, 'w') as f:
            print(f"Created file: {filename}")
    except Exception as e:
        print(f"Error creating file: {e}")

def makedir(dirname):
    # GUYS WHAT DOES THIS DO?
    try:
        os.makedirs(dirname)
        print(f"Created directory: {dirname}")
    except Exception as e:
        print(f"Error creating directory: {e}")

def delfile(filename):
    # omg i am trying to find what this does
    try:
        os.remove(filename)
        print(f"Deleted file: {filename}")
    except Exception as e:
        print(f"promblemo with getting rid of {filename}, error: {e}")

def deldir(dirname):
    # and this too.....
    try:
        shutil.rmtree(dirname)
        print(f"got rid of {dirname}")
    except Exception as e:
        print(f"error with getting rid of {dirname}, error: {e}")

def custom_ls():
    try:
        # it gets the parent directory name and path and then lists the files :thumbsup:
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        files = os.listdir(parent_dir)
        for file in files:
            print(file)
    except Exception as e:
        print(f"we got a lil problemo with listing a file.. error: {e}")

