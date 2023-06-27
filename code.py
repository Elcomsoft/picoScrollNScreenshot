import pwmio
from board import LED
import usb_hid
import time

from adafruit_hid.keyboard import Keyboard                   # lib/adafruit_hid
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS # lib/adafruit_hid
from adafruit_hid.keycode import Keycode                     # lib/adafruit_hid
from adafruit_hid.mouse import Mouse                   # lib/adafruit_hid

led = pwmio.PWMOut(LED, frequency=5000, duty_cycle=0)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
mouse = Mouse(usb_hid.devices)

SCROLL_MOUSE_DISTANCE = 250 #negative number scrolls upwards
SCROLL_WITH_MOUSE = 1 #set to 1 for mouse or 0 for keyboard
DELAY_AFTER_SCROLL = 1 #interval (in seconds) between scroll and screen shot

def doScreenshot():
    global kbd
    kbd.press(Keycode.SHIFT)
    kbd.press(Keycode.GUI)
    kbd.press(layout.keycodes('3')[0])
    kbd.release_all()

def doScroll_keyboard():
    global kbd
    kbd.press(Keycode.PAGE_DOWN)
    kbd.release_all()
    
def doScroll_mouse():
    mouse.move(wheel=SCROLL_MOUSE_DISTANCE)
    
def doScroll():
    if SCROLL_WITH_MOUSE:
        return doScroll_mouse()
    else:
        return doScroll_keyboard()

def led_up():
    global led
    led.duty_cycle = 65535

def led_down():
    global led
    led.duty_cycle = 0

def main():
    for i in range(15):
        led_up()
        time.sleep(.5)
        led_down()
        time.sleep(.5)

    while True:
        led_up()
        doScreenshot()
        time.sleep(1)
        led_down()
        doScroll()
        time.sleep(DELAY_AFTER_SCROLL)

main()
