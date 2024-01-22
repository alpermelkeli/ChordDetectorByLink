# Python code to convert video to audio
import sys
import os
import time

import moviepy.editor as mp


videoFile = sys.argv[1]
audioFile = sys.argv[2]


# Insert Local Video File Path 
clip = mp.VideoFileClip(rf"{videoFile}")

# Insert Local Audio File Path
clip.audio.write_audiofile(rf"{audioFile}")

