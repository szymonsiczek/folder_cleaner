import os, shutil

print('Unpack files from subfolders of:')
folder = input()
destination = folder

# Unpack files from subfolders:
foldernamesList = []
for folderName, subfolders, filenames in os.walk(folder):
  foldernamesList.append(folderName)
  for item in os.listdir(folderName):
      file = os.path.join(folderName, item)
      if os.path.dirname(file) != destination:
          shutil.move(file, destination)
          
# Delete empty folders          
for emptyFolder in range(len(foldernamesList)):
    if foldernamesList[-1] != folder:
        os.rmdir(foldernamesList[-1])
        del foldernamesList[-1]
