import time
import pwmio
import board
import digitalio
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)
led = pwmio.PWMOut(board.LED)
keyboard = Keyboard(usb_hid.devices)
write_text = KeyboardLayoutUS(keyboard)



btn1_pin = board.GP0
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
def payload():
    time.sleep(0.1)
    #enter your payload here



    
     
if btn1.value:
    led.duty_cycle = 2 ** 15
    time.sleep(1)
else:
    time.sleep(2.5)
    led.duty_cycle = 2 ** 15
    payload()
        
    
time.sleep(0.1)
