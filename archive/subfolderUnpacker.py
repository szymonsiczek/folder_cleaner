import os
import shutil

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
