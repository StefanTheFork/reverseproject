#sewer v1
import os
import shutil

def sewerdo(args):
    print(f"DEBUG: received argument = {args}")
    try:
        if args[0] == "-i":
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
                    os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject temp")
                    package = package + ".py"
        
                    if os.path.exists(os.path.join("temp", "packages", package)):
                        shutil.move(os.path.join("temp", "packages", package), package)
                        print(f"moved your {package} into the thing")
                        print("cleaning up...")
                        shutil.rmtree("temp")
                        print("cleaned up...")
                        print("installation was succsessful!")

                except Exception as e:
                    print("sorry but it wasnt installed. error:",e)
        
        elif args[0] == "-us":
            os.makedirs("temp",)
            os.makedirs("temp2",)

            print("Updating sewer... this will take a moment or two")
            print("Cloning reverseproject repository")
            os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git temp")

            if os.path.exists("packages/sewer.py"):
                shutil.move("packages/sewer.py", os.path.join("temp2", "sewer_backup.py"))
                print("Backed up sewer")
            else:
                print("Sewer not found in parent folder")

            if os.path.exists(os.path.join("temp", "packages/sewer.py")):
                shutil.move(os.path.join("temp", "packages/sewer.py"), "packages/sewer.py")
                print("Moved new pkg to parent folder")
            else:
                print("Updated sewer not found in temp folder")

        elif args[0] == "-ub":
            os.makedirs("temp", exist_ok=True)
            os.makedirs("temp2", exist_ok=True)

            print("Cloning repository")
            os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git temp")

            if os.path.exists("base.py"):
                shutil.move("base.py", os.path.join("temp2", "base_backup.py"))
                print("Backed up base.py")
            else:
                print("base.py not found in parent folder")

            if os.path.exists(os.path.join("temp", "base.py")):
                shutil.move(os.path.join("temp", "base.py"), "base.py")
                print("Moved updated base.py to parent folder")
            else:
                print("Updated base.py not found in temp folder")

        else:
            print("Unknown command. Usage: sewer <-i package; -us; -ub>")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if os.path.exists("temp"):
            try:
                shutil.rmtree("temp")
                print("Cleaned up temp folder")
            except Exception as cleanup_err:
                print(f"Failed to remove temp folder: {cleanup_err}")

        if os.path.exists("temp2"):
            try:
                shutil.rmtree("temp2")
                print("Cleaned up temp2 folder")
            except Exception as cleanup_err:
                print(f"Failed to remove temp2 folder: {cleanup_err}")


    
