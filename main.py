import tca9534
import sys

from machine import Pin
import time
print("input value for config register by hex value ")
print("example : 0F (7-4 output,3-0 input")
print("value for config register: ")
bitmask = sys.stdin.readline()
value = int(bitmask, 16)
dev = tca9534.TCA9534(tca9534_address=0x20,scl=Pin(42), sda=Pin(41), bitmask=value)  # ESP32-S3
#dev = tca9534.TCA9534(tca9534_address=0x20, output=True)  # initialize all pins to be outputs
# dev = tca9534.TCA9534(bitmask=0b01110011) # initialize w/ specific inputs and outputs enabled
while(1):
    print("1: Read all config")
    print("2: Set output for a pin")
    print("3: Get input")
    print("Your choice: ", end="")

    bitmask = sys.stdin.readline().strip()  # Read input and remove any extra whitespace or newline characters

    # Process the user's choice
    if bitmask == '1':
        # Call the method to read all configuration registers
        config, output, input_val = dev.show_all_registers()
        print(f"configuration register: {config[0]:08b}")
        print(f"output register: {output[0]:08b}")
        print(f"input register: {input_val[0]:08b}")

    elif bitmask == '2':
        # Prompt for additional input to set the output for a specific pin
        print("Enter pin number and state (e.g., '3 1' to set pin 3 to high): ")
        pin_state = sys.stdin.readline().strip()
        pin, state = map(int, pin_state.split())  # Split and convert input to integers
        print(f"Pin {pin} set to {'high' if state else 'low'}.")
        dev.write_pin(pin, state)  # Assuming you have a method to set the pin state
        
    elif bitmask == '3':
        # Call the method to get input from a pin or input register
        print("Enter pin number to get state (e.g., '1' to get input from pin 1): ")
        pin_state = sys.stdin.readline().strip()
        pin = int(pin_state)
        state = dev.read_pin(pin)  # Removed unnecessary semicolon
        print(f"Pin {pin} is {'high' if state else 'low'}.")
    else:
        print("Invalid choice, please select 1, 2, or 3.")
