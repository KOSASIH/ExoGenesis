import os
import shutil
import datetime

def backupCodebase(source_directory, backup_directory):
    """
    Creates a backup of the entire codebase, including source code, documentation, and assets, for archival purposes.

    Parameters:
    source_directory (str): The path to the source directory of the codebase.
    backup_directory (str): The path to the backup directory where the backup will be stored.
    """

    # Create the backup directory if it doesn't exist
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    # Get the current date and time for the backup filename
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"codebase_backup_{current_datetime}.zip"

    # Create a zip archive of the source directory
    shutil.make_archive(os.path.join(backup_directory, backup_filename), 'zip', source_directory)

    print(f"Backup of codebase created at {os.path.join(backup_directory, backup_filename)}")
