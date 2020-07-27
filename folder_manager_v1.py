from pathlib import Path
import os
import shutil


def findFileTypesInFolder(folder):
    finalListofFileTypes = []
    for filename in os.listdir(folder):
        suffix = Path(os.path.join(folderToClean, filename)).suffix.strip('.')
        if suffix not in finalListofFileTypes:
            finalListofFileTypes.append(suffix)
    return finalListofFileTypes


def getSuffixWithoutDot(file):
    path_file = Path(os.path.join(folderToClean, file))
    file_suffix = path_file.suffix
    suffix_without_dot = file_suffix.strip('.')
    return suffix_without_dot


def separate_and_strip_file_types(string):
    listOfFilesToClean = string.split(', ')
    for file in listOfFilesToClean:
        listOfFilesToClean[listOfFilesToClean.index(file)] = file.strip()
    return listOfFilesToClean


def folder_cleaner():
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
                    shutil.move(
                        (os.path.join(folderToClean, filename)), newFolder)


def automatic_folder_cleaner():
    # Ask user which folder needs to be cleaned
    print('Please enter the absolute path of a folder, that needs to be cleaned:')
    folderToClean = input()
    # Define file types in a given folder
    finalListOfFileTypes = findFileTypesInFolder(folderToClean)
    # Create a new folder for every type of file
    for filetype in finalListOfFileTypes:
        newFolder = (os.path.join(folderToClean, (filetype.lower())))
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)
        # Segregate files into acuurate folders
        for filename in os.listdir(folderToClean):
            if os.path.isfile(os.path.join(folderToClean, filename)):
                if getSuffixWithoutDot(filename).lower() == filetype.lower():
                    shutil.move(
                        (os.path.join(folderToClean, filename)), newFolder)


def subfolder_unpacker():
    print('Unpack files from subfolders of:')
    folder = input()
    destination = folder
    # Unpack files from subfolders:
    foldernamesList = []
    for folderName, subfolders, filenames in os.walk(folder):
        foldernamesList.append(folderName)
    for folderName in foldernamesList:
        for item in os.listdir(folderName):
            file = os.path.join(folderName, item)
            if os.path.dirname(file) != destination:
                try:
                    shutil.move(file, destination)
                except shutil.Error:
                    newName = 'unpacked_' + item
                    os.rename(file, os.path.join(folderName, (newName)))
                    file = os.path.join(folderName, (newName))
                    shutil.move(file, destination)
    # Delete empty folders
    for emptyFolder in (foldernamesList):
        if emptyFolder != folder:
            try:
                os.rmdir(emptyFolder)
            except OSError:
                continue


automatic_folder_cleaner()
