import time
import RPi.GPIO as GPIO

# use Broadcom pin numbers
GPIO.setmode(GPIO.BCM)

SERVO_PIN = 3

GPIO.setup(SERVO_PIN, GPIO.OUT)

# setup PWM 
pwm = GPIO.PWM(SERVO_PIN, 100)

pwm.start(5)

for i in range(5, 25):
  pwm.ChangeDutyCycle(i)
  time.sleep(0.5)

pwm.stop()
GPIO.cleanup()
