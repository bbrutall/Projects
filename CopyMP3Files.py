import shutil
import os
import random

PARENT_PATH = ''
COPY_PATH = ''
COUNT_TRACKS = 20
music_list =[]
new_list = []

def CopyRandomMusic():
    """copy random music"""
    
    for top, dirs, files in os.walk(PARENT_PATH):
        for nm in files:
            if os.path.join(top, nm)[-4: len(os.path.join(top, nm))] == '.mp3':
                music_list.append(os.path.join(top, nm))

    for i, m  in zip(range(0, COUNT_TRACKS), music_list):
        if m not in new_list:
            new_list.append(music_list[random.randint(0,len(music_list))])

    for music_file in new_list:
         shutil.copy2(music_file, COPY_PATH)

CopyRandomMusic()
