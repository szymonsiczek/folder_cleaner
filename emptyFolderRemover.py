
import os

print('Please enter an absolute path to a folder, in which you want to delete empty subfolders.')
folder = input()
foldernamesList = []
for foldername, subfolders, filename in os.walk(folder):
    foldernamesList.append(foldername)
    
for emptyFolder in (foldernamesList):
    if emptyFolder != folder:
        try:
            os.rmdir(emptyFolder)    
        except OSError:
            continue

