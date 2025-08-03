# Stupid Package Manager v1.4
# changes: slight rewrite 
import os
import shutil

def update_package():
    print("what do you want to update?")
    print("1. update base")
    print("2. update spm")

    choice = input("enter 1 or 2: ").strip()

    if choice == "1":
        target_file = "base.py"
        backup_file = "base_backup.py"
        print("updating base...")

    elif choice == "2":
        target_file = "spm.py"
        backup_file = "spm_backup.py"
        print("updating spm...")

    else:
        print("invalid choice.")
        return

    print("cloning repository...")
    os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git useless")

    if os.path.exists(target_file):
        shutil.move(target_file, os.path.join("backups", backup_file))
        print(f"backed up {target_file} as {backup_file}.")
    else:
        print(f"{target_file} not found in parent folder.")

    updated_path = os.path.join("useless", target_file)
    if os.path.exists(updated_path):
        shutil.move(updated_path, target_file)
        print(f"moved updated {target_file} to parent folder.")
    else:
        print(f"updated {target_file} not found in repository folder.")

    print("cleaning up...")
    shutil.rmtree("useless")
    os.makedirs("useless", exist_ok=True)
    print("cleaned up.")

def install():
    try:
        package = input("enter pkg name ~> ").strip()

        if not package:
            print("hey i cant install        !")
            return

        if not package.endswith(".py"):
            package += ".py"

        print("cloning repo...")
        os.system("git clone --depth 1 --single-branch --branch main https://github.com/StefanTheFork/reverseproject.git useless")

        pkg_path = os.path.join("useless", "packages", package)
        if os.path.exists(pkg_path):
            shutil.move(pkg_path, package)
            print(f"moved '{package}' into current directory.")
            print("cleaning up...")
            shutil.rmtree("useless") 
            os.makedirs("useless", exist_ok=True)
            print("cleaned up.")
            print("great success")
    except Exception as e:
        print(f"hey uh there seems to be an error..... Error: {e}")
