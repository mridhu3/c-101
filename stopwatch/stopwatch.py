import time
from playsound import playsound
stop = int(input("time in seconds :"))
while stop > 0:
        min = int(stop/60)
        secs = int(stop%60)
        timer = f'{min}:{secs}'
        print(timer)
        stop-=1
print("You're Time'S Up")
playsound("mixkit-sound.wav")



