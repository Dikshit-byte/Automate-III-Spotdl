import os
import glob
import shutil
import subprocess
from pathlib import Path

source = 'C:\\Python\\Spotdlfy\\dl'
destination = str(Path.home()/"Music")
link = input("Enter the link of playlist , song, or album : ")
subprocess.run(f'spotidl {link}')

allfile = glob.glob(os.path.join(source,'*.mp3*'),recursive = True)
print("File to move",allfile)

#for all files in dl folder to move into music folder
for file_path in allfile:
    dst_path = os.path.join(destination,os.path.basename(file_path))
    shutil.move(file_path,dst_path)
    print(f'Moved {file_path} -> {dst_path}')
