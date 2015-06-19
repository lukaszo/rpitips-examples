import time
import wiringpi2 as wiringpi

#use Broadcom pin numbers
wiringpi.wiringPiSetupGpio()

LED_PIN = 25

# setup pin as an output
wiringpi.pinMode(LED_PIN, 1)

while True:
  # enable LED
  wiringpi.digitalWrite(LED_PIN, 1)

  # wait 1 second
  time.sleep(1)

  # disable LED
  wiringpi.digitalWrite(LED_PIN, 0)

  # wait 1 second
  time.sleep(1)

#cleanup
wiringpi.pinMode(LED_PIN, 0)
