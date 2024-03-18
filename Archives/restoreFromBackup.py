import os
import shutil

def restoreFromBackup(backup_path, restore_path):
    """
    Restores the project from a previous backup in case of data loss or corruption.

    Parameters:
    backup_path (str): The path to the backup directory.
    restore_path (str): The path to the directory where the backup will be restored.

    Returns:
    bool: True if the restoration was successful, False otherwise.
    """
    # Check if the backup directory exists
    if not os.path.isdir(backup_path):
        print(f"Error: Backup directory '{backup_path}' does not exist.")
        return False

    # Check if the restore path exists
    if os.path.isdir(restore_path):
        answer = input(f"Warning: Restore path '{restore_path}' already exists. Do you want to overwrite it? (y/n) ")
        if answer.lower() != 'y':
            print("Restoration cancelled.")
            return False
        shutil.rmtree(restore_path)

    # Extract the backup to the restore path
    shutil.unpack_archive(os.path.join(backup_path, 'backup.zip'), restore_path)

    print("Restoration successful.")
    return True
