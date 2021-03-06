#! python3
# This program segregates files in a given folder
# into a folders named after the type of files

from pathlib import Path
import os
import shutil

os.chdir(r'C:\Users\User\Dropbox\Python\my_projects')


def separate_and_strip_file_types(string):
    listOfFilesToClean = string.split(', ')
    for file in listOfFilesToClean:
        listOfFilesToClean[listOfFilesToClean.index(file)] = file.strip()
    return listOfFilesToClean


def getSuffixWithoutDot(file):
    path_file = Path(os.path.join(folderToClean, file))
    file_suffix = path_file.suffix
    suffix_without_dot = file_suffix.strip('.')
    return suffix_without_dot


# Ask user which folder needs to be cleaned
print('Please enter the absolute path of a folder, that needs to be cleaned:')
folderToClean = input()

# Ask user what types of files have to be cleaned
while True:
    print('\nPlease define what kind of files would you like to segregate. Pass them below with commas and spaces but without dots. Here is an example: "jpg, pdf, docx, zip".\n(OrPress "CTRL + C" to escape.)')
    fileTypesToClean = input()
    finalListOfFileTypes = separate_and_strip_file_types(fileTypesToClean)

    # Create a new folder for every type of file
    for filetype in finalListOfFileTypes:
        newFolder = (os.path.join(folderToClean, (filetype.lower())))
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)
        # Segregate files into acuurate folders
        for filename in os.listdir(folderToClean):
            if getSuffixWithoutDot(filename).lower() == filetype.lower():
                shutil.move((os.path.join(folderToClean, filename)), newFolder)
