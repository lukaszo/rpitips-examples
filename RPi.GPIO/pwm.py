import time

import RPi.GPIO as GPIO

#use Broadcom pin numbers
GPIO.setmode(GPIO.BCM)

SERVO_PIN = 3

# configure output on pin
GPIO.setup(SERVO_PIN, GPIO.OUT)

#setup PWM, set frequency to 100Hz
pwm = GPIO.PWM(SERVO_PIN, 100)

# start PWM with duty cycle 5% 
pwm.start(5)

while True:
  # increase duty cycle by 5, it will speed up the motor
  # or will increase LED brightness
  for i in range(5, 100, 5):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.5)

  # decrease duty cycle by 5, it will slow down the motor
  # or will decrease LED brightness
  for i in range(100, 5, -5):
    pwm.ChangeDutyCycle(i)
    time.sleep(0.5)

pwm.stop()
