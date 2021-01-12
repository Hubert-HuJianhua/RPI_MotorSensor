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
    if GPIO.input(A):
        if not GPIO.input(B):
            spin_count += 1
        elif GPIO.input(B):
            spin_count -= 1
    print(spin_count)


GPIO.add_event_detect(A, GPIO.RISING, callback=my_callback)
while True:
    print("Runing")
    time.sleep(1)
