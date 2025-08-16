import os
import shutil
from datetime import datetime

time = datetime.now()

'''
Welcome to the devbuild of v1 quaso
v1 quaso implements ACTUAL config files (TAKE THAT CARROT CAKE!)
the good thing about these config files is that you can edit them LIVE
unlike the base, where you have to exit it, open an ide to edit like 3 lines and then repeat.
the config files contain everything youll need to run 3rd party functions, like and exec imports system
aswell as a exec commands system.


this will be the last BIG feature update (for now, atleast)
i am going to be focusing on packages like 
envy (a vim/gnu nano style text editor)
cowsay reverse port
fortune reverse port

new features that ARENT going to be new packages are:
uninstalling packages using spm and sewer. (this is a feature that you geniunely might need, thats why im adding it to spm)
logo in config file. 
the reason why im not adding them rn is because its 5:44am and i am in need of sleep.
'''


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
        os.makedirs(dirname)
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
    print(f"Editing {filename}. Type 'end' on a new line to save and exit.")
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

# Config system
commands = {}

def load_config(config_file="dev_config.txt"):
    global commands
    commands = {}
    try:
        print(f"Looking for config file: {config_file}")
        with open(config_file, 'r') as f:
            lines = f.readlines()
        
        print(f"Read {len(lines)} lines from config")
        
        # Get the main module's globals to inject imports there
        import sys
        main_globals = sys.modules[__name__].__dict__
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                # Handle imports
                if line.startswith('import ') or line.startswith('from '):
                    try:
                        exec(line, main_globals)
                        #print(f"Imported: {line}")
                    except Exception as e:
                        print(f"Import error: {line} - {e}")
                # Handle commands
                elif ' - ' in line:
                    cmd, func_call = line.split(' - ', 1)
                    commands[cmd.strip()] = func_call.strip()
                    #print(f"Added command: {cmd.strip()} -> {func_call.strip()}")
        
        print(f"Loaded {len(commands)} commands from config")
        
    except FileNotFoundError:
        print(f"Config file {config_file} not found - creating default config")
        create_default_config(config_file)
    except Exception as e:
        print(f"Error loading config: {e}")

def create_default_config(config_file="dev_config.txt"):
    default_config = """# DevBuild Configuration File
# Format: command - function_call()

# Imports
import os
import shutil
from datetime import datetime
import spm
import sewer
import minifetch
import funnifetch
import editor


# cant go nowehere without mah clock and clear :broken heart:
clear - clear_screen()
clock - clock()

# File operations
mkfile - mkfile()
mkdir - mkdir()
rmfile - rmfile()
rmdir - rmdir()
cat - readfile()
edit - editfile()

# SPM and sewer handling
spm-install - spm.install()
spm-update - spm.update_package()
sewer - sewer.sewerdo()

# Sysfetch stuff
minifetch - minifetch.sysfetch()
funnifetch - funnifetch.fetch()

"""
    
    try:
        with open(config_file, 'w') as f:
            f.write(default_config)
        print(f"Created default config file: {config_file}")
        load_config(config_file)  # Reload after creating
    except Exception as e:
        print(f"Error creating config file: {e}")


def reload_config():
    print("Reloading config...")
    load_config()

def execute_imports(func_call, args):
    try:
        # Handle imported module functions with global scope
        if '(' in func_call and ')' in func_call:
            # Function call - execute with globals so imports are available
            exec(func_call, globals())
        else:
            # Simple expression - evaluate with globals
            result = eval(func_call, globals())
            if result is not None:
                print(result)
        
    except NameError as e:
        print(f"Module/function not found: {e}")
        print("Make sure to import the module in your config file")
    except Exception as e:
        print(f"Error executing command: {e}")


def execute_command(func_call, args):
    try:
        import sys
        main_globals = sys.modules[__name__].__dict__
        
        # Handle function calls that need args
        if '()' in func_call and args:
            # Remove the () and replace with args
            func_name = func_call.replace('()', '')
            if func_name in ['mkfile', 'mkdir', 'rmfile', 'rmdir', 'editfile']:
                if len(args) == 1:
                    exec(f"{func_name}('{args[0]}')", main_globals)
                else:
                    print(f"Usage: command <argument>")
            elif func_name == 'readfile':
                exec(f"readfile({args})", main_globals)
            elif func_name == 'sewer.sewerdo':
                exec(f"sewer.sewerdo({args})", main_globals)
            else:
                # throw spaghetti at wall
                exec(f"{func_name}({args})", main_globals)
        else:
            # for custom func
            exec(func_call, main_globals)
            
    except NameError as e:
        print(f"Function/module not found: {e}")
        print("Make sure to import the module in your config file")
    except Exception as e:
        print(f"Error executing command: {e}")

def devshell():
    asciilogo = """
    DEVBUILD OF v1 quaso
 _ __ _____   _____ _ __ ___  ___  
| '__/ _ \ \ / / _ \ '__/ __|/ _ \  
| | |  __/\ V /  __/ |  \__ \  __/_ 
|_|  \___| \_/ \___|_|  |___/\___(_)
     use help to get help(?)
"""
    print(asciilogo)
    
    # Load initial config
    load_config()

    while True:
        command = input("-> ").strip()
        if not command:
            continue 

        parts = command.split()
        func_name = parts[0]
        args = parts[1:]

        if func_name == "reload":
            reload_config()
        elif func_name == "help":
            print("Available commands:")
            for cmd in commands:
                print(f"  {cmd}")
            print("  reload - reload config")
            print("  help - show this help")
        elif func_name in commands:
            execute_command(commands[func_name], args)
        else:
            print(f"Unknown command: {func_name}")

clear_screen()
devshell()
