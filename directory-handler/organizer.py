# This file must be inside the directory you want to organize. Make sure this extensions are added 
# in the .gitignore file to avoid uploading this files to the repo.
# To test this program, copy several files with different formats (extensions) within 
# "directory-handler" directory, then run this program.

# Look up the current directory files and move them into corresponding subdirectories 

import os
from pathlib import Path

SUBDIRECTORIES = {
    "documents": ['.docx', '.txt', '.pdf'],
    "videos": ['.mov', '.avi', '.mp4'],
    "images": ['.png', '.jpeg', '.jpg'],
    "audio": ['.m4a', '.m4b', '.mp3']
}

# Identify the right subdirectory for the extension given
def pickDirectory(format):
    for directory, extensions in SUBDIRECTORIES.items():
        # If format is in extensions for the current directory then return directory
        if format in extensions:
            return directory
    # If there is no extension that matches with the given format, then return an altrnative directory
    return "others"

# Take the file path in the directory, then create (if not exists) and move the 
# file to the corresponding directory
def moveFiles():
    for file in os.scandir():
        # If the object is file, skip iteration
        if file.is_dir() or '.py' in file.__fspath__():
            continue
        filepath = Path(file)
        filetype = filepath.suffix.lower()
        directory = pickDirectory(filetype)
        directorypath = Path(directory)
        # If the directory path does not exist, create it
        if directorypath.is_dir() != True:
             directorypath.mkdir()
        # Move the file to the corresponding directory
        filepath.rename(directorypath.joinpath(filepath))

moveFiles()