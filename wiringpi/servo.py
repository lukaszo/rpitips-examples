import wiringpi2 as wiringpi

#use Broadcom pin numbers
wiringpi.wiringPiSetupGpio()

SERVO_PIN = 25

# setup pin as an output
wiringpi.pinMode(SERVO_PIN, 1)

# setup PWM 
wiringpi.softPwmCreate(SERVO_PIN, 0, 100)

# change duty cycle
wiringpi.softPwmWrite(SERVO_PIN, 1)
wiringpi.delay(200)
wiringpi.softPwmWrite(SERVO_PIN, 20)
wiringpi.delay(200)
