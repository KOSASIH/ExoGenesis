import os
import shutil

def archiveOldVersions(archive_directory, project_directory, version_pattern):
    """
    Archives old versions of the project's codebase, documentation, and assets to declutter the current working directory.
    
    Parameters:
    archive_directory (str): The directory where the archived versions will be stored.
    project_directory (str): The directory containing the current version of the project.
    version_pattern (str): A pattern to identify old versions of the project.
    
    Returns:
    None
    """
    
    # Create the archive directory if it doesn't exist
    if not os.path.exists(archive_directory):
        os.makedirs(archive_directory)
    
    # Iterate over the files and directories in the project directory
    for item in os.listdir(project_directory):
        
        # Check if the item matches the version pattern
        if version_pattern in item:
            
            # Create a new directory for the archived version
            archived_version_directory = os.path.join(archive_directory, item)
            os.makedirs(archived_version_directory)
            
            # Move the old version to the archive directory
            old_version_path = os.path.join(project_directory, item)
            shutil.move(old_version_path, archived_version_directory)
