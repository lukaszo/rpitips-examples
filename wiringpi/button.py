import time
import wiringpi2 as wiringpi

# use Broadcom pin numbers
wiringpi.wiringPiSetupGpio()

BUTTON_PIN = 25

# confiure pin as input
wiringpi.pinMode(BUTTON_PIN, 0)

while True:
  # print bin state
  print wiringpi.digitalRead(BUTTON_PIN)
  time.sleep(1)
