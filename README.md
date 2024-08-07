# TCA9534 8-bit i2c GPIO library

### Default address: 0x27  

# Default speed 400000
# scl pin : scl=Pin(9), sda=Pin(8)

Use `show_all_registers()` to see the current status of the device

Use `set_pin(pin)` to write `pin` HIGH

Use `clear_pin(pin)` to write `pin` LOW

Use `read_pin(pin)` as you would expect

output example :

no bitmask, setting up all channels

...for write

set pin:  0

current_outputs: 00110000

updated current_outputs: 00110001

clear pin:  0

current_outputs: 00110001

updated current_outputs: 00110000

set pin:  1

current_outputs: 00110000

updated current_outputs: 00110010

clear pin:  1

current_outputs: 00110010

updated current_outputs: 00110000

set pin:  2

current_outputs: 00110000

updated current_outputs: 00110100

clear pin:  2

current_outputs: 00110100

updated current_outputs: 00110000

set pin:  3

current_outputs: 00110000

updated current_outputs: 00111000

clear pin:  3

current_outputs: 00111000

updated current_outputs: 00110000

set pin:  4

need to set this channel to OUTPUT, new config:  00110000

current_outputs: 00110000

updated current_outputs: 00110000

clear pin:  4

need to set this channel to OUTPUT, new config:  00110000

current_outputs: 00110000

updated current_outputs: 00100000

set pin:  5

need to set this channel to OUTPUT, new config:  00110000

current_outputs: 00100000

updated current_outputs: 00100000

clear pin:  5

need to set this channel to OUTPUT, new config:  00110000

current_outputs: 00100000

updated current_outputs: 00000000

set pin:  6

current_outputs: 00000000

updated current_outputs: 01000000

clear pin:  6

current_outputs: 01000000

updated current_outputs: 00000000

set pin:  7
current_outputs: 00000000
updated current_outputs: 10000000
clear pin:  7
current_outputs: 10000000
updated current_outputs: 00000000