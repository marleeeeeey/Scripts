import RPi.GPIO as GPIO
import time

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

SPEED_MIN = 80
SPEED_MAX = 100
SPEED_STEP = 1

speed = SPEED_MIN
step = SPEED_STEP

while True:
        if speed >= SPEED_MAX:
            speed = SPEED_MAX
            step = -SPEED_STEP
        elif speed < SPEED_MIN:
            speed = SPEED_MIN
            step = SPEED_STEP
        speed += step
        print(speed)
        duty_s = speed
        duty = int(duty_s)
        pwm_led.ChangeDutyCycle(duty)
        time.sleep(0.1)

