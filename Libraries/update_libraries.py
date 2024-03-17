import subprocess
import json

def update_libraries():
    """Updates third-party libraries to their latest versions to incorporate bug fixes and new features."""
    
    # Get the list of installed libraries and their current versions
    installed_libraries = get_installed_libraries()
    
    # Get the latest versions of the libraries from the package manager
    latest_versions = get_latest_library_versions()
    
    # Update the libraries to their latest versions
    updated_libraries = []
    for library in installed_libraries:
        latest_version = latest_versions.get(library['name'])
        if latest_version and library['version'] != latest_version:
            update_library(library['name'], latest_version)
            updated_libraries.append({'name': library['name'], 'old_version': library['version'], 'new_version': latest_version})
    
    return updated_libraries

def get_installed_libraries():
    """Gets the list of installed libraries and their current versions."""
    
    # Run the command to list installed libraries and their versions
    command = 'pip freeze'
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    
    # Parse the output to get the list of installed libraries and their versions
    installed_libraries = []
    for line in output.split('\n'):
        if line:
            library_name, library_version = line.split('==')
            installed_libraries.append({'name': library_name, 'version': library_version})
    
    return installed_libraries

def get_latest_library_versions():
    """Gets the latest versions of the libraries from the package manager."""
    
    # Run the command to get the latest versions of the libraries
    command = 'pip search --json --outdated'
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    
    # Parse the output to get the latest versions of the libraries
    latest_versions = {}
    for line in output.split('\n'):
if line:
            data = json.loads(line)
            library_name = data['name']
            latest_version = data['latest_version']
            latest_versions[library_name] = latest_version
    
    return latest_versions

def update_library(library_name, latest_version):
    """Updates a library to its latest version."""
    
    # Run the command to update the library
    command = f'pip install {library_name}=={latest_version}'
    subprocess.run(command, shell=True, check=True)
