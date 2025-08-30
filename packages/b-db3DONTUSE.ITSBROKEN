import os
import shutil
from datetime import datetime
import sys

time = datetime.now()

'''
Welcome to reverse v1 devbuild 3
v1 implements ACTUAL config files (TAKE THAT CARROT CAKE!)

most important features on devbuild 3:
the base editor is no more

'''

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

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

# ooooooooo configs........
commands = {}
variables = {}
def load_config(config_file="config.rvrs"):
    global commands
    commands = {}
    try:
        print(f"Looking for config file: {config_file}")
        with open(config_file, 'r') as f:
            lines = f.readlines()
        
        print(f"Read {len(lines)} lines from config")
        
        # get imports (i think?)
        main_globals = sys.modules[__name__].__dict__
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                # imports mmmmmmm
                if line.startswith('import ') or line.startswith('from '):
                    try:
                        exec(line, main_globals)
                    except Exception as e:
                        print(f"Import error: {line} - {e}")
                # komand. 
                elif ' - ' in line:
                    cmd, func_call = line.split(' - ', 1)
                    commands[cmd.strip()] = func_call.strip()
        
        print(f"loaded {len(commands)} commands from config")
        
    except FileNotFoundError:
        print(f"Config file {config_file} not found - creating default config")
        create_default_config(config_file)
    except Exception as e:
        print(f"Error loading config: {e}")

def reload_config_debug(config_file="config.rvrs"): # this is a separate function because i couldnt figure out how to actaulyl make it work properly.
    load_config()
    with open(config_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            if line.startswith('import'):
                print(line)
            elif ' - ' in line:
                print(line)

def create_default_config(config_file="config.rvrs"):
    default_config = """# Reverse Configuration File
# Format: alias - function()

# Imports
import os
import shutil
from datetime import datetime
import spm
import sewer

# file stuff.
mkfile - mkfile()
mkdir - mkdir()
rmfile - rmfile()
rmdir - rmdir()
cat - readfile()
edit - editfile()

# spm stuff
spm-install - spm.install()
spm-update - spm.update_package()
sewer - sewer.sewerdo()

# other stuff
reload-debug - reload_config_debug()
"""
    try:
        with open(config_file, 'w') as f:
            f.write(default_config)
        print(f"Created default config file: {config_file}")
        load_config(config_file)  #load after creating
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
        main_globals = sys.modules[__name__].__dict__
        
        # if it got args itll do the do
        if '()' in func_call and args:
            # remove the parenthassdhsdhisdsidjes and replace them with the argument
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
            # throw spaghetti at wall pt2
            exec(func_call, main_globals)

        
            
    except NameError as e:
        print(f"Function/module not found: {e}")
        print("Make sure to import the module in your config file")
    except Exception as e:
        print(f"Error executing command: {e}")

def shell():
    asciilogo = """
 _ __ _____   _____ _ __ ___  ___  
| '__/ _ \ \ / / _ \ '__/ __|/ _ \  
| | |  __/\ V /  __/ |  \__ \  __/_ 
|_|  \___| \_/ \db3|_|  |___/\___(_)
they see me rollin.... they hatin...
"""

    info = """
PLEASE NOTE THAT COMMANDS WITH SPACES IN THEM DONT WORK!
if you have a command that has a space (lets say something like spm install)
youll need to add a dash inside your config. this will be fixed in the next update.
    """
    showinfo = 1
    print(asciilogo)
    print("Welcome to the funny.")
    if showinfo == 1:
        print(info)
    else:
        pass

    # good golly gee, what could this do?
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
        elif func_name == "clear":
            clear()
        elif func_name == "clock":
            clock()
        elif func_name == "logo":
            print(asciilogo)
        elif func_name == "help":
            print("Available commands:")
            for cmd in commands:
                print(f"  {cmd}")
            print("  reload - reload config")
            print("  reload -debug - reloads config and shows the commands and imports.")
            print("  help - show this thingy")
        elif func_name in commands:
            execute_command(commands[func_name], args)
        else:
            print(f"Unknown command: {func_name}")

clear()
shell()
