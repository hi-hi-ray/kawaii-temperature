import RPi.GPIO as GPIO
import time

def flashing_light():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) 
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.8)
	GPIO.output(18, GPIO.LOW)
	GPIO.cleanup()  