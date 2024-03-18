import os
import json

def remove_unused_dependencies(package_json_path):
    """
    Removes unused dependencies from the project to reduce bloat and improve performance.

    :param package_json_path: Path to the package.json file.
    """

    # Load the package.json file
    with open(package_json_path, 'r') as file:
        package_json = json.load(file)

    # Get the list of dependencies
    dependencies = package_json.get('dependencies', {})

    # Get the list of files in the project
    project_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.js') or file.endswith('.ts'):
                project_files.append(os.path.join(root, file))

    # Analyze the code to identify unused dependencies
    unused_dependencies = []
    for dependency in dependencies:
        if not any(dependency in file for file in project_files):
            unused_dependencies.append(dependency)

    # Remove the unused dependencies from the package.json file
    for dependency in unused_dependencies:
        del package_json['dependencies'][dependency]

    # Save the updated package.json file
    with open(package_json_path, 'w') as file:
        json.dump(package_json, file, indent=2)

    print(f"Removed {len(unused_dependencies)} unused dependencies.")
