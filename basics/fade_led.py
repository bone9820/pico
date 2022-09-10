import utime
from machine import Pin, PWM

board_led = Pin("LED", Pin.OUT)
eye_led = Pin(15, Pin.OUT)

pwm = PWM(eye_led)

pwm.freq(1000)

duty = 0
direction = 1
for repeat in range(2000):
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1

    pwm.duty_u16(duty * duty)
    utime.sleep(0.01)
