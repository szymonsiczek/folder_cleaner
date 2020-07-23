#! python3
# This program segregates files in a given folder
# into a folders named after the type of files

from pathlib import Path
import os, shutil

def findFileTypesInFolder(folder):
    finalListofFileTypes = []
    for filename in os.listdir(folder):
        suffix = Path(os.path.join(folderToClean, filename)).suffix.strip('.')
        if suffix not in finalListofFileTypes:
            finalListofFileTypes.append(suffix)
    return finalListofFileTypes

def getSuffixWithoutDot(file):
    return Path(os.path.join(folderToClean, file)).suffix.strip('.')
    

# Ask user which folder needs to be cleaned 
print('Please enter the absolute path of a folder, that needs to be cleaned:')
folderToClean = input()

# Define file types in a given folder
finalListOfFileTypes = findFileTypesInFolder(folderToClean)

# Create a new folder for every type of file
for filetype in finalListOfFileTypes:
    newFolder =(os.path.join(folderToClean, (filetype.lower())))
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)

    # Segregate files into acuurate folders
    for filename in os.listdir(folderToClean):
        if os.path.isfile(os.path.join(folderToClean,filename)):
            if getSuffixWithoutDot(filename).lower() == filetype.lower():
                shutil.move((os.path.join(folderToClean,filename)), newFolder)
         
