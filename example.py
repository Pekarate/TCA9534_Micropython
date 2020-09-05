import tca9534
import time

dev = tca9534.TCA9534(output=True)

while True:
    for i in range(8):
        dev.set_pin(i)
        time.sleep(1)
        dev.clear_pin(i)
    time.sleep(5)
