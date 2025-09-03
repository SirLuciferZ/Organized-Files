"""
File Organizer Script

This script organizes files in a specified directory by sorting them into subfolders
based on their file extensions. Each file type gets its own folder, named after its
extension (e.g., `.txt`, `.jpg`, `.pdf`).

When executed:
    - It scans the target folder for files (ignoring subdirectories).
    - Creates a new folder for each unique file extension if it doesn't already exist.
    - Moves files into their corresponding extension-based folders.
    - Logs all operations (folder creation, file movement, replacements) in a `log.txt`
      file located one directory above the target folder.
    - Prompts the user before overwriting files with the same name in the destination.

Features:
    - Automatic categorization of files by extension.
    - Prevention of accidental overwrites with user confirmation.
    - Detailed logging of all file operations with timestamps.
    - Skips directories and processes only files.

Requirements:
    - Python 3.x
    - No external libraries required (uses built-in `os`, `shutil`, and `datetime` modules).

Author: SirLuciferZ
Date: 2025/09/01
"""

import os
import shutil
from datetime import datetime

# Change the working directory to the folder containing files to be organized
#   I'm recommending to create a new folder for the files to orginize
PATH = r"e:\.Dev\.Development\Project\Python\Organized Files\Files"  #  Add your file path here

os.chdir(PATH)

# Current timestamp for logging file operations
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def has_files_only(item_path):
    """
    Check if the given directory contains at least one file.

    Args:
        path (str): Path to the directory to check.

    Returns:
        bool: True if at least one file exists in the directory, False otherwise.

    Notes:
        - This function ignores subdirectories and only checks for files.
        - Stops checking as soon as it finds the first file.
    """
    for item in os.listdir(item_path):
        full_path = os.path.join(item_path, item)
        if os.path.isfile(full_path):
            return True
    return False


def select_files_only(selected_path):
    """
    Determine if the given path is a file.

    Args:
        path (str): Path to check.

    Returns:
        bool: True if the path points to a file, False otherwise.

    Notes:
        - This is used to filter out directories when iterating over os.listdir().
    """
    return os.path.isfile(selected_path)


# Get the current working directory (folder containing files to organize)
folder_path = os.getcwd()

# If no files are found, prompt the user to add files before proceeding
if not has_files_only(folder_path):
    print(
        "\nNo files found in the directory. Please add files to the directory before organizing.\n"
    )

else:
    # Open the log file in append mode to record file operations
    # f = open("../log.txt", "a", encoding="utf-8")
    with open("../log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\nFILES EDITED AT {now}\n\n")

        # Iterate over all items in the directory
        for file in os.listdir():
            if select_files_only(file):
                # Extract file extension to use as folder name
                foldername = os.path.splitext(file)[1]
                NEW_PATH = rf"{folder_path}\{foldername}"

                # If the folder for this file type already exists
                if os.path.exists(NEW_PATH):
                    # If the file already exists in the destination folder
                    if os.path.exists(rf"{NEW_PATH}\{file}"):
                        choice = input(
                            f"\n{file} already exists in \n{NEW_PATH}. \n \
                                Do you want to overwrite it? (y/n): "
                        )
                        if choice.lower() == "y":
                            os.remove(rf"{NEW_PATH}\{file}")
                            shutil.move(file, NEW_PATH)
                            f.write(f"{file} replaced in {NEW_PATH}\n")
                        else:
                            print("\nFile not overwritten")
                    else:
                        # Move file to existing folder
                        shutil.move(file, NEW_PATH)
                        f.write(f"{file} moved to {NEW_PATH}\n")

                else:
                    # Create a new folder for this file type
                    os.mkdir(NEW_PATH)
                    f.write(f"{NEW_PATH} created\n")
                    shutil.move(file, NEW_PATH)
                    f.write(f"{file} moved to {NEW_PATH}\n")

            else:
                # Skip directories or non-file items
                continue

    # Close the log file after all operations
    # f.close()
    print("\nFiles organized successfully\n")
