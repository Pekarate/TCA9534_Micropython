import tca9534
import time

dev = tca9534.TCA9534()

while True:
    i = 0
    while i < 8:
        dev.set_pin(i)
        i += 1
        time.sleep(0.5)
    i = 0
    while i < 8:
        dev.clear_pin(i)
        i += 1
        time.sleep(0.5)
    i = 0
    while i < 8:
        dev.read_pin(i)
        i += 1
        time.sleep(1)
