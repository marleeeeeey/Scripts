import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

while (True):
	GPIO.output(18, True)
	GPIO.output(17, False)
	time.sleep(0.5)
	GPIO.output(18, False)
	GPIO.output(17, True)
	time.sleep(0.5)
