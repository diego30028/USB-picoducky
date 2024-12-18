import time
import board
import digitalio
import usb_hid
from adafruit_hid.keycode_es import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_es import KeyboardLayout
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
time.sleep(2.5)
# Set up Consumer Control - Control Codes can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/consumer_control_code.html#ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)

# Set up a keyboard device. - Keycode can be found here: https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
keyboard = Keyboard(usb_hid.devices)

# Set up keyboard to write strings from macro
write_text = KeyboardLayout(keyboard)



btn1_pin = board.GP0
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
def payload():
    #enter your payload here




    
    
    # Keycode class defines USB HID keycodes to send using Keyboard.  
if btn1.value:
   print("edit mode")
else:
    payload()
        
    
time.sleep(0.1)
