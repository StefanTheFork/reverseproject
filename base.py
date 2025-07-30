# base v0.9.1, changes: base text editor and base text reading command and some other stuff i think
import os
import shutil
from datetime import datetime
time = datetime.now()

# if your host os is unix, use clear, if windows use cls, if it cant find what you have it just prints 100 new lines
if os.name == 'posix':
    clear = "clear"
elif os.name == 'nt':
    clear = "cls"
else:
    print('\n' * 100)

# BASE commands

def filesys(argument):
    if argument == "create":
        folders = ['user', 'backups', 'useless']
        for folder in folders:
            os.makedirs(folder, exist_ok=True)
            print(f"maked {folder}")
        print("file system is ready!")
    elif argument == "decimate":
        folders = ['user', 'backups', 'useless']
        for folder in folders:
            shutil.rmtree(folder)
            print(f"got rid of {folder}")
        print("destroyed successfully!")

def clear_screen():
    os.system(clear)

def clock():
    current_time = time.strftime("%H:%M:%S")
    print(current_time)

def makefile(filename):
    try:
        with open(filename, 'w') as f:
            print(f"Created file: {filename}")
    except Exception as e:
        print(f"Error creating file: {e}")

def makedir(dirname):
    try:
        os.makedirs(dirname)
        print(f"Created directory: {dirname}")
    except Exception as e:
        print(f"Error creating directory: {e}")

def delfile(filename):
    try:
        os.remove(filename)
        print(f"Deleted {filename}")
    except Exception as e:
        print(f"Error with deleting file {filename}, error: {e}")

def deldir(dirname):
    try:
        shutil.rmtree(dirname)
        print(f"Removed {dirname}")
    except Exception as e:
        print(f"Error with removing directory {dirname}, error: {e}")

def readfile(filenames):
    for file in filenames:
        try:
            with open(file, 'r') as f:
                print(f.read(), end='')  # No extra newline
        except FileNotFoundError:
            print(f"cat: {file}: No such file or directory")
        except PermissionError:
            print(f"cat: {file}: Permission denied")
        except Exception as e:
            print(f"cat: {file}: Error - {e}")

def editfile(filename):
    print(f"Editing {filename}. Type ':wq' or 'EOF' on a new line to save and exit.")
    lines = []

    try:
        # Load existing contents if file exists
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                old_lines = f.readlines()
            print("--------CURRENT FILE CONTENT---------")
            for line in old_lines:
                print(line, end='')
            print("\n--- START TYPING BELOW ---")

        # Read new content
        while True:
            line = input()
            if line.strip() in (':wq', 'EOF'):
                break
            lines.append(line)

        # Write new content to file
        with open(filename, 'w') as f:
            f.write('\n'.join(lines) + '\n')
        print(f"Saved {filename}")

    except Exception as e:
        print(f"Error editing file: {e}")

# fallback shell

def fallbackshell():
    print("hey, you havent set up a shell!")
    print("fear not my child. here is a fallback shell")

    while True:
        command = input("~> ").strip()
        if not command:
            continue 

        parts = command.split()
        func_name = parts[0]
        args = parts[1:]

        if func_name == "filesys":
            if len(args) != 1:
                print("Usage: filesys <create|decimate>")
            else:
                filesys(args[0])

        elif func_name == "clear":
            clear_screen()

        elif func_name == "clock":
            clock()

        elif func_name == "makefile":
            if len(args) != 1:
                print("Usage: makefile <filename>")
            else:
                makefile(args[0])

        elif func_name == "makedir":
            if len(args) != 1:
                print("Usage: makedir <dirname>")
            else:
                makedir(args[0])

        elif func_name == "delfile":
            if len(args) != 1:
                print("Usage: delfile <filename>")
            else:
                delfile(args[0])

        elif func_name == "deldir":
            if len(args) != 1:
                print("Usage: deldir <dirname>")
            else:
                deldir(args[0])

        elif func_name == "read":
            if not args:
                print("Usage: read <file>")
            else:
                readfile(args)

        elif func_name == "edit":
            if len(args) != 1:
                print("Usage: edit <filename>")
            else:
                editfile(args[0])
clear_screen()
fallbackshell()
