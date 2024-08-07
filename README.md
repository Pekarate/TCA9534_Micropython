# TCA9534 8-bit i2c GPIO library

#### Default address: 0x27  
#### Default speed 400000
#### scl pin : scl=Pin(9), sda=Pin(8)

Use `show_all_registers()` to see the current status of the device
Use `set_pin(pin)` to write `pin` HIGH

Use `clear_pin(pin)` to write `pin` LOW

Use `read_pin(pin)` as you would expect

Tested 
   MicroPython v1.23.0 on 2024-06-02; Generic ESP32S3 module with ESP32S3
   MicroPython v1.23.0 on 2024-06-02; Raspberry Pi Pico with RP2040

output example :
![Screenshot 2024-08-08 001252](https://github.com/user-attachments/assets/046c80dc-03a7-4a54-9d6e-222f1fa401d5)
