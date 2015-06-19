import time
import RPi.GPIO as GPIO


# use Broadcom pin numbers
GPIO.setmode(GPIO.BCM)

BUTTON_PIN = 4

GPIO.setup(BUTTON_PIN, GPIO.IN)

while True:
  # print bin state
  print GPIO.input(BUTTON_PIN)
  time.sleep(1)

GPIO.cleanup()
