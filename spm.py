# Stupid Package Manager v1.1.
# changes: replaced all mentions of kernel with base and rephrased the backing up base thing
import os
import shutil

def update_base():
    print("cloning repository")
    os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git useless")

def finalize_base_update():
    if os.path.exists("base.py"):
        shutil.move("base.py", os.path.join("backups", "base_backup.py"))
        print("backed up base.py...")
    else:
        print("base.py not found in parent folder")
    if os.path.exists(os.path.join("useless", "base.py")):
        shutil.move(os.path.join("useless", "base.py"), "base.py")
        print("moved updated base.py to parent folder..")
    else:
        print("updated base.py not found in useless folder...")

def cleanup():
    print("cleaning up...")
    shutil.rmtree("useless")
    print("deleted useless folder...")
    os.makedirs("useless")
    print("recreated useless folder...")

