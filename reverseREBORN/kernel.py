import os

def setup_filesystem():
    folders = ['user', 'backups', 'updates', 'useless']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    print("file system is ready!")

def kill_filesystem():
    folders = ['user', 'backups', 'updates', 'useless']
    for folder in folders:
        os.rmdir(folder)
        print(f"Removed folder: {folder}")

    print("destroyed successfully!")

def clear_screen():
    # Clear screen command based on OS
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        # If the OS is not recognized, print a newline
        print('\n' * 100)
