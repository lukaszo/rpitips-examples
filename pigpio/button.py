import time

import pigpio


LED_PIN = 25

#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(LED_PIN, pigpio.INPUT)

while True:
  # print bin state
  print pi.read(LED_PIN)
  time.sleep(1)

#disconnect
pi.stop()
