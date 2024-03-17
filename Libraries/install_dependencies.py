import os
import subprocess

def install_dependencies():
    """
    Installs project dependencies listed in the package.json or requirements.txt file.
    """
    if os.path.exists('package.json'):
        print("Installing dependencies from package.json...")
        subprocess.run(['npm', 'install'], check=True)
    elif os.path.exists('requirements.txt'):
        print("Installing dependencies from requirements.txt...")
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
    else:
        print("No package.json or requirements.txt file found. Please provide a package.json or requirements.txt file to install dependencies.")
