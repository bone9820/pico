from time import sleep
from machine import Pin, PWM

board_led = Pin("LED", Pin.OUT)

pin14 = Pin(14)
pin15 = Pin(15)

left_eye = PWM(pin14)
right_eye = PWM(pin15)

left_eye.freq(1000)
right_eye.freq(1000)


def eyes_off():
    left_eye.duty_u16(0)
    right_eye.duty_u16(0)


def eyes_on():
    left_eye.duty_u16(65536)
    right_eye.duty_u16(65536)


def pulse_eyes(times):
    for x in range(times):
        duty = 0
        direction = 1
        for i in range(512):
            duty += direction
            if duty > 255:
                duty = 255
                direction = -1
            elif duty < 0:
                duty = 0
                direction = 1

            left_eye.duty_u16(duty * duty)
            right_eye.duty_u16(duty * duty)
            sleep(.01)


def initialize():
    eyes_off()
    board_led.off()
    board_led.on()


initialize()
pulse_eyes(3)
eyes_on()
print('online')
