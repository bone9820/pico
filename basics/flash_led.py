from machine import Pin, Timer

board_led = Pin("LED", Pin.OUT)
eye_led = Pin(15, Pin.OUT)

timer = Timer()


def blink(timer):
    board_led.toggle()
    eye_led.toggle()


timer.init(freq=10, mode=Timer.PERIODIC, callback=blink)
