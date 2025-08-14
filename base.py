# base v0.9, changes: renamed a shitload of stuff, fallback shell now has ascii art and uh native spm support wowza
import os
import shutil
from datetime import datetime
import spm
time = datetime.now()

if os.name == 'posix':
    clear = "clear"
elif os.name == 'nt':
    clear = "cls"
else:
    print('\n' * 100)

# BASE commands
def clear_screen():
    os.system(clear)

def clock():
    current_time = time.strftime("%H:%M:%S")
    print(current_time)

def mkfile(filename):
    try:
        with open(filename, 'w') as f:
            print(f"Created file: {filename}")
    except Exception as e:
        print(f"Error creating file: {e}")

def mkdir(dirname):
    try:
        os.mkdirs(dirname)
        print(f"Created directory: {dirname}")
    except Exception as e:
        print(f"Error creating directory: {e}")

def rmfile(filename):
    try:
        os.remove(filename)
        print(f"Deleted {filename}")
    except Exception as e:
        print(f"Error with deleting file {filename}, error: {e}")

def rmdir(dirname):
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
            if line.strip() in ("end"):
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
    fallback = """
   __      _ _ _                _    
  / _|    | | | |              | |   
 | |_ __ _| | | |__   __ _  ___| | __
 |  _/ _` | | | '_ \ / _` |/ __| |/ /
 | || (_| | | | |_) | (_| | (__|   < 
 |_| \__,_|_|_|_.__/ \__,_|\___|_|\_\\
"""
    print(fallback)
    print("hey, you havent set up a shell!")
    print("fear not my child. for i have.... a fallback shell")

    while True:
        command = input("~> ").strip()
        if not command:
            continue 

        parts = command.split()
        func_name = parts[0]
        args = parts[1:]

        if func_name in ("clr", "clear", "cls"):
            clear_screen()

        elif func_name == "clock":
            clock()

        elif func_name == "mkfile":
            if len(args) != 1:
                print("Usage: mkfile <filename>")
            else:
                mkfile(args[0])

        elif func_name == "mkdir":
            if len(args) != 1:
                print("Usage: mkdir <dirname>")
            else:
                mkdir(args[0])

        elif func_name == "rmfile":
            if len(args) != 1:
                print("Usage: rmfile <filename>")
            else:
                rmfile(args[0])

        elif func_name == "rmdir":
            if len(args) != 1:
                print("Usage: rmdir <dirname>")
            else:
                rmdir(args[0])

        elif func_name == "cat":
            if not args:
                print("Usage: read <file>")
            else:
                readfile(args)

        elif func_name == "edit":
            if len(args) != 1:
                print("Usage: edit <filename>")
            else:
                editfile(args[0])

        elif command == "spm install":
            spm.install()

        elif command == "spm update":
            spm.update_package()

clear_screen()
fallbackshell()
