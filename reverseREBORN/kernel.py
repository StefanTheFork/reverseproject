import os

def onboot():
    print("hello world")
    #example onboot entry. put kernel.onboot() in your shell file as a standalone line and you can execute stuff like a logo or clock thing.

def setup_filesystem():
    #creates beautiful file system
    folders = ['user', 'backups', 'useless']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    print("file system is ready!")

def kill_filesystem():
    #sudo rm -rf / --no-preserve-root, but doesnt delete kernel, shell or package manager
    folders = ['user', 'backups', 'useless']
    for folder in folders:
        os.rmdir(folder)
        print(f"Removed folder: {folder}")

    print("destroyed successfully!")

def clear_screen():
    # scans if you got unix, funni finnish man os or bill gates operating system
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        # if it cant decide if youre running one of those it just goes batshit and prints a new line 100 times i think
        print('\n' * 100)
