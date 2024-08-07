# TCA9534 8-bit i2c GPIO library

#### Default address: 0x27  
#### Default speed 400000
#### scl pin : scl=Pin(9), sda=Pin(8)

Use `show_all_registers()` to see the current status of the device
Use `set_pin(pin)` to write `pin` HIGH
Use `clear_pin(pin)` to write `pin` LOW
Use `read_pin(pin)` as you would expect

output example :
![Screenshot 2024-08-07 231954](https://github.com/user-attachments/assets/5615a829-3dca-4a05-98fb-f6e4c4dc6d7a)
