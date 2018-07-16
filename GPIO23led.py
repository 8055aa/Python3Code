#!/usr/bin/env python3

#This is RPI.GPIO test

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 23
GPIO.setup(led, GPIO.OUT)

try:
    while(True):
        GPIO.output(led, 1)
        time.sleep(2)
        GPIO.output(led, 0)
        time.sleep(1)
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
