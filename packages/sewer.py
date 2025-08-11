# sewer v1. very work in progress
import os
import shutil

def sewerdo(args):
    if args[0] == "-us":
        os.makedirs("temp","backups")
        print("updating sewer.... this will take a moment, or two")
        print("cloning reverseproject repository")
        os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git temp")

        if os.path.exists("sewer.py"):
            shutil.move("sewer.py", os.path.join("backups", "sewer_backup.py"))
            print("backed up sewer")
        else:
            print("sewer not found in parent folder")
    
        if os.path.exists(os.path.join("temp", "sewer.py")):
            shutil.move(os.path.join("temp", "sewer.py"), "sewer.py")
            print("moved new pkg to parent folder..")
        else:
            print("updated sewer found in temp folder...")

        print("cleaning up...")
        shutil.rmtree("temp")
        print("cleaned up...")

    elif args[0] == "-ub":
        os.makedirs("backups", "temp")
        print("cloning repository")
        os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git temp")
    
        if os.path.exists("base.py"):
            shutil.move("base.py", os.path.join("backups", "base_backup.py"))
            print("backed up base.py...")
        else:
            print("base.py not found in parent folder")
        if os.path.exists(os.path.join("temp", "base.py")):
            shutil.move(os.path.join("temp", "base.py"), "base.py")
            print("moved updated base.py to parent folder..")
        else:
            print("updated base.py not found in temp folder...")

        print("cleaning up...")
        shutil.rmtree("temp")
        print("cleaned up...")

    elif args[0] == "-i":
        os.makedirs("temp")
        if len(args) < 2:
            print("Please specify a package to install.")
            return
        package = args[1]
        if package == "":
            print("there isnt a package to download.")
        else: 
            try:
                print("cloning repository")
                os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git temp")
                package = package + ".py"
    
                if os.path.exists(os.path.join("temp", "packages", package)):
                    shutil.move(os.path.join("temp", "packages", package), package)
                    print("moved your " + package + " into the thing")
                    print("cleaning up...")
                    shutil.rmtree("temp")
                    print("cleaned up...")
                    print("installation was succsessful!")

            except Exception as e:
                print("sorry but it wasnt installed. error:",e)
        
    
