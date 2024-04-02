# Stupid Package Manager v1.0
import os
import shutil

def update_kernel():
    print("cloning repository")
    os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git useless")

def finalize_kernel_update():
    if os.path.exists("kernel.py"):
        shutil.move("kernel.py", os.path.join("backups", "kernel_backup.py"))
        print("moved current kernel.py to backups folder")
    else:
        print("kernel.py not found in parent folder")
    if os.path.exists(os.path.join("useless", "kernel.py")):
        shutil.move(os.path.join("useless", "kernel.py"), "kernel.py")
        print("moved updated kernel.py to parent folder..")
    else:
        print("updated kernel.py not found in useless folder...")

def cleanup():
    print("cleaning up...")
    shutil.rmtree("useless")
    print("deleted useless folder...")
    os.makedirs("useless")
    print("recreated useless folder...")

