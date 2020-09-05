import tca9534
import time

dev = tca9534.TCA9534(output=True) # initialize all pins to be outputs
# dev = tca9534.TCA9534(bitmask=0b01110011) # initialize w/ specific inputs and outputs enabled

while True:
    for i in range(8):
        dev.write_pin(i, 1)
        # dev.set_pin(i)
        time.sleep(1)
        dev.write_pin(i, 0)
        # dev.clear_pin(i)
    time.sleep(5)
