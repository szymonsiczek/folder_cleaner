import os
import shutil
import send2trash

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
                send2trash.send2trash(os.path.join(destination, item))
                shutil.move(file, destination)

# Delete empty folders
for emptyFolder in (foldernamesList):
    if emptyFolder != folder:
        try:
            os.rmdir(emptyFolder)
        except OSError:
            continue
