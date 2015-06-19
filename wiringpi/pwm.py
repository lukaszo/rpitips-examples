import wiringpi2 as wiringpi

#use Broadcom pin numbers
wiringpi.wiringPiSetupGpio()

SERVO_PIN = 25

# configure output on pin
wiringpi.pinMode(SERVO_PIN, 1)

# setup PWM 
wiringpi.softPwmCreate(SERVO_PIN, 0, 100)

while True:
  # increase duty cycle by 5, it will speed up the motor
  # or will increase LED brightness
  for i in range(5, 100, 5):
    wiringpi.softPwmWrite(SERVO_PIN, i)
    wiringpi.delay(500)

  # decrease duty cycle by 5, it will slow down the motor
  # or will decrease LED brightness
  for i in range(100, 5, -5):
    wiringpi.softPwmWrite(SERVO_PIN, i)
    wiringpi.delay(500)
