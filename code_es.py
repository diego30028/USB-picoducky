import time
import pwmio
import board
import digitalio
import usb_hid
from adafruit_hid.keycode_es import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_es import KeyboardLayout
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)
led = pwmio.PWMOut(board.LED)
write_text = KeyboardLayout(keyboard)


btn1_pin = board.GP0
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
def payload():
    #enter you payload here
  
if btn1.value:
    led.duty_cycle = 2 ** 15
    time.sleep(1)
else:
    time.sleep(2.5)
    led.duty_cycle = 2 ** 15 
    payload()
time.sleep(0.1)
