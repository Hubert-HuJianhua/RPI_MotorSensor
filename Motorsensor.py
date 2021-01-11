import RPi.GPIO as GPIO
import time


spin_count = 0
A = 21
B = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(A, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    global spin_count
    if not GPIO.input(A):
        if not GPIO.input(B):
            spin_count += 1
        else:
            spin_count -= 1
    else:
        if not GPIO.input(A):
            spin_count += 1
        else:
            spin_count -= 1
    print(spin_count)


GPIO.add_event_detect(A, GPIO.FALLING, callback=my_callback, bouncetime=20)
while True:
    print("runing")
    time.sleep(1)
# while True:
#
#     print(count)
#     time.sleep(0.02)
