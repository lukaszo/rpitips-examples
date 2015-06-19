import time
import pigpio

LED_PIN = 25

#connect to pigpiod daemon
pi = pigpio.pi()

# setup pin as an output
pi.set_mode(LED_PIN, pigpio.OUTPUT)

# pi set frequency
pi.set_PWM_frequency(24, 100)

while True:
  while True:
    # increase duty cycle by 5, it will speed up the motor
    # or will increase LED brightness
    for i in range(5, 100, 5):
        pi.set_PWM_dutycycle(23,i);time.sleep(0.1)

    # decrease duty cycle by 5, it will slow down the motor
    # or will decrease LED brightness
    for i in range(100, 5, -5):
        pi.set_PWM_dutycycle(23,i);time.sleep(0.1)

#cleanup
pi.set_mode(LED_PIN, pigpio.INPUT)
#disconnect
pi.stop()
