import RPi.GPIO as GPIO
import time

GPIO.setup(18, GPIO.OUT)

while (True):
   GPIO.output(i, True)
   time.sleep(0.5)
   GPIO.output(i, False)
   time.sleep(0.5)
