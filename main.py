import json
import requests
import time
import os
from datetime import datetime
import random

# main functions

def chimeIn(song):
        song_list = ['bye.m4a', 'mmmhhh.m4a', 'nice.m4a', 'sure.m4a']
        os.system('omxplayer ' + song_list[song])


# while loop
while True: 
    number = random.randint(0,3)
    chimeIn(number)
    time.sleep(150)