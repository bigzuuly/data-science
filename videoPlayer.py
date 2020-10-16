##!/usr/bin/env python

import json
import io
import os
import vlc
import time

# SETUP
#------------------------------------
RESOURCES_DIR = "./resources/videos/small_400_400/"
# Load json file
matrixFile = open(os.path.join(os.getcwd(),'resources','matrix.json'), 'r')
matrixData = matrixFile.read()

matrixFile.close()

# Convert json file into python dictionary
matrixDic = json.loads(matrixData)

#vlc init
vlc_instance = vlc.Instance("--intf dummy --vout mmal_vout --aout alsa --alsa-audio-device output")
player = vlc_instance.media_player_new()

def displayVideoMenu():
  print("Video #\t Video File")
  for index in range(len(matrixDic["items"])):
    print (index, "\t", matrixDic["items"][index]["filename"])

  print ("\n#################################\n")


def playMedia(media_uri, loop):
  global player
  player.pause()
  media = vlc_instance.media_new(media_uri)
  if(loop == True): #add loop to default player
    media.add_options("input-repeat=65535")

  player.set_media(media)
  player.play()

  if (loop != True): #loop video should be non-blocking
    time.sleep(1.5) #need to buffer a bit before calculating duration
    duration = player.get_length() / 1000
    time.sleep(duration)


while True:
  displayVideoMenu()
  value = int(input("Please enter a video number:\n"))
  playMedia(os.path.join(RESOURCES_DIR, matrixDic["items"][value]["filename"]), False)
