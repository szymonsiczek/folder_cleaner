from pathlib import Path
import os
import shutil


def folder_to_clean():
    print('Please enter the absolute path of a folder, that you want to work with:')
    folder_to_clean = input()
    return folder_to_clean


def menu():
    print('\nChoose operation type: \n 1.Automatic folder cleaner\n 2.Clean folder file-type by file-type\n 3.Unpack files from subfolders\n\n(Press CTRL+C to end program)')
    choice = input()
    if choice == '1':
        automatic_folder_cleaner()
        menu()
    elif choice == '2':
        folder_cleaner()
    elif choice == '3':
        subfolder_unpacker()
        menu()


def find_file_types_in_folder(folder_to_clean):
    finalListofFileTypes = []
    for filename in os.listdir(folder_to_clean):
        suffix = Path(os.path.join(folder_to_clean, filename)
                      ).suffix.strip('.')
        if suffix not in finalListofFileTypes:
            finalListofFileTypes.append(suffix)
    return finalListofFileTypes


def get_suffix_without_dot(file):
    path_file = Path(os.path.join(folder_to_clean, file))
    file_suffix = path_file.suffix
    suffix_without_dot = file_suffix.strip('.')
    return suffix_without_dot


def separate_and_strip_file_types(string):
    listOfFilesToClean = string.split(', ')
    for file in listOfFilesToClean:
        listOfFilesToClean[listOfFilesToClean.index(file)] = file.strip()
    return listOfFilesToClean


def folder_cleaner():
    # Ask user what types of files have to be cleaned
    while True:
        print('\nPlease define what kind of files would you like to segregate. Pass them below with commas and spaces but without dots. Here is an example: "jpg, pdf, docx, zip".\n(Or type MENU to go back to menu.)')
        fileTypesToClean = input()
        if fileTypesToClean.lower() == 'menu':
            menu()
        finalListOfFileTypes = separate_and_strip_file_types(fileTypesToClean)
        # Create a new folder for every type of file
        for filetype in finalListOfFileTypes:
            newFolder = (os.path.join(folder_to_clean, (filetype.lower())))
            if not os.path.exists(newFolder):
                os.makedirs(newFolder)
            # Segregate files into acuurate folders
            for filename in os.listdir(folder_to_clean):
                if get_suffix_without_dot(filename).lower() == filetype.lower():
                    shutil.move(
                        (os.path.join(folder_to_clean, filename)), newFolder)


def automatic_folder_cleaner():
    # Define file types in a given folder
    finalListOfFileTypes = find_file_types_in_folder(folder_to_clean)
    # Create a new folder for every type of file
    for filetype in finalListOfFileTypes:
        newFolder = (os.path.join(folder_to_clean, (filetype.lower())))
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)
        # Segregate files into acuurate folders
        for filename in os.listdir(folder_to_clean):
            if os.path.isfile(os.path.join(folder_to_clean, filename)):
                if get_suffix_without_dot(filename).lower() == filetype.lower():
                    shutil.move(
                        (os.path.join(folder_to_clean, filename)), newFolder)


def subfolder_unpacker():
    destination = folder_to_clean
    # Unpack files from subfolders:
    foldernamesList = []
    for folderName, subfolders, filenames in os.walk(folder_to_clean):
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
        if emptyFolder != folder_to_clean:
            try:
                os.rmdir(emptyFolder)
            except OSError:
                continue


folder_to_clean = folder_to_clean()
menu()
