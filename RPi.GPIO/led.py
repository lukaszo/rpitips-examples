import time

import RPi.GPIO as GPIO


#use Broadcom pin numbers
GPIO.setmode(GPIO.BCM)

LED_PIN = 3

# setup pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
  # enable LED
  GPIO.output(LED_PIN, GPIO.HIGH)

  # wait 1 second
  time.sleep(1)

  # disable LED
  GPIO.output(LED_PIN, GPIO.LOW)
  time.sleep(1)

GPIO.cleanup()
