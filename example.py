# i2c = I2C(0,scl=Pin(9), sda=Pin(8), freq=400_000)   # default assignment: scl=Pin(9), sda=Pin(8)
# print(i2c.scan())
import tca9534
import time
from machine import Pin

dev = tca9534.TCA9534(tca9534_address=0x20,scl=Pin(42), sda=Pin(41), output=True)  # ESP32-S3
#dev = tca9534.TCA9534(tca9534_address=0x20, output=True)  # initialize all pins to be outputs 
# dev = tca9534.TCA9534(bitmask=0b01110011) # initialize w/ specific inputs and outputs enabled

for i in range(8):
    dev.write_pin(i, 1)
    # dev.set_pin(i)
    time.sleep(1)
    dev.write_pin(i, 0)
    # dev.clear_pin(i)
    time.sleep(1)
