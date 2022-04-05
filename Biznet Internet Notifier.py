from pythonping import ping
import os
from mutagen.mp3 import MP3
import time


def pinging():
    domain = input('Input the domain to use (Default Google) : ')
    baseline = input('Input the highest ping to wait (Default 50) : ')
    if not domain:
        domain = '8.8.8.8'
    if not baseline:
        baseline = 50
    for sound in os.listdir('.'):
        if sound.endswith('.mp3'):
            mp3use = sound
            mp3time = MP3(mp3use)
            break
        else:
            print('No mp3 file to use')
    os.system('cls')
    while True:
        response = ping(domain, count=5)
        if response.rtt_avg_ms <= float(baseline):
            os.system(mp3use)
            time.sleep(int(mp3time.info.length))
        else:
            os.system('cls')
            avg = response.rtt_avg_ms
            print('Biznet Ping Notifier')
            print()
            print('Current Average Ping Is ' + str(avg) + ' Above The Set Threshold ' + str(baseline))


pinging()