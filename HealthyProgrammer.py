'''
9AM - 5PM
Water - water.mp3 (3.5 L or 250ml every 30min) - Drank - log
Eyes - eyes.mp3 - every 30 min - EyDone - log
Physical Activity - physical.mp3 every - 45 min -ExDone - log
'''
o = open("Health.txt" , "+a")
from pygame import mixer
mixer.init()
from datetime import *
x = datetime.strptime("11/03/22 14:23" , "%d/%m/%y %H:%M")
h = int(str(x.time())[0:2])
while h >= 9 and h < 17:
    print(h)
    mixer.music.load("water.mp3")
    mixer.music.set_volume(0.7)
    import time
    time.sleep(1)
    mixer.music.play()
    i = input("Drank Likho bhai")
    if i == "Drank":
        mixer.music.stop()
        timenow = time.asctime(time.localtime(time.time()))
        o.write(f"Drank Water at {timenow}")
        break
    mixer.music.load("eye.mp3")
    mixer.music.set_volume(0.7)
    import time
    time.sleep(1)
    mixer.music.play()
    i = input("EyDone Likho bhai")
    if i == "EyDone":
        mixer.music.stop()
        timenow = time.asctime(time.localtime(time.time()))
        o.write(f"Eye Exercise done at {timenow}")
        break
    mixer.music.load("physical.mp3")
    mixer.music.set_volume(0.7)
    import time
    time.sleep(1)
    mixer.music.play()
    i = input("ExDone Likho bhai")
    if i == "ExDone":
        mixer.music.stop()
        timenow = time.asctime(time.localtime(time.time()))
        o.write(f"Exercise Done at {timenow}")
        break
    """Bas Break ko hta do toh Program 'chalta hi rahega aur time apne hissaab se adjust kr lo"""