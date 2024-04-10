# Stupid Package Manager Core v1.3.1
# changes: automatic cleanup wow
import os
import shutil

def spm_update_base():
    print("cloning repository")
    os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git useless")
    
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

    # HOLY SH*T AUTOMATIC CLEANUP ON BASE UPDATE? YOURE KIDDING ME!
    print("cleaning up...")
    shutil.rmtree("useless")
    os.makedirs("useless")
    print("cleaned up...")

def update_spm_core():
    print("updating spm core.. this will take a moment, or two")
    print("cloning repository")
    os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git useless")

    if os.path.exists("spm.py"):
        shutil.move("spm.py", os.path.join("backups", "spm_backup.py"))
        print("backed up current spm")
    else:
        print("spm not found in parent folder")
    
    if os.path.exists(os.path.join("useless", "spm.py")):
        shutil.move(os.path.join("useless", "spm.py"), "spm.py")
        print("moved updated spm to parent folder..")
    else:
        print("updated spm not found in useless folder...")

    # LOOK AT THIS. AUTOMATIC CLEANUP! 
    print("cleaning up...")
    shutil.rmtree("useless")
    os.makedirs("useless")
    print("cleaned up...")

def spm_installpkg(package):
    try:
        print("cloning repository")
        os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git useless")
    
        if os.path.exists(os.path.join("useless", "packages", package)):
            shutil.move(os.path.join("useless", "packages", package), package)
            print("moved your " + package + " into the thing")
            print("cleaning up...")
            shutil.rmtree("useless")
            os.makedirs("useless")
            print("cleaned up...")
            print("installation was succsessful!")


        else:
            print("yk, sometimes packages just dont exist, or you forgot the .py on the end...")

    except Exception as e:
        print("sorry but it wasnt installed. error:",e)
