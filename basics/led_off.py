from machine import Pin, Timer

board_led = Pin("LED", Pin.OUT)
eye_led = Pin(15, Pin.OUT)

board_led.off()
eye_led.off()