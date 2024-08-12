
"""Interface with the Qwiic GPIO board, a TCA9534 I/O expander.

Set and read 8 digitalchannels.
TCA9534 datasheet:
https://www.ti.com/lit/ds/symlink/tca9534.pdf
QWIIC GPIO board:
https://github.com/sparkfunX/Qwiic_GPIO

by hoang4.tran 08/08/2024
"""
from machine import Pin, I2C


class TCA9534:
    """Instance of TCA9534 I/O expander."""

    REGISTER_INPUT_PORT = 0x00    # register 0
    REGISTER_OUTPUT_PORT = 0X01    # register 1
    REGISTER_CONFIGURATION = 0X03    # register 3

    def __init__(self, i2c_ch=0, tca9534_address=0x27,scl=Pin(9), sda=Pin(8),freq=400_000 ,output=True, bitmask=None):
        """Default values taken from Sparkfun QWIIC GPIO board."""
        self.address = tca9534_address
        self.bus = I2C(i2c_ch,scl=scl, sda=sda, freq=freq)
        if bitmask:
            bitmasks = bitmask.to_bytes(1, 'big')
            self.bus.writeto_mem(self.address, self.REGISTER_CONFIGURATION, bitmasks)
            return
        if output:
            # set all 8 channels to OUTPUT by writing 0
            self.bus.writeto_mem(self.address, self.REGISTER_CONFIGURATION, bytes([0x00]))
            self.bus.writeto_mem(self.address, self.REGISTER_OUTPUT_PORT, bytes([0x00]))
        else:
            # set all 8 channels to INPUT by writing 1
            self.bus.writeto_mem(self.address, self.REGISTER_CONFIGURATION, bytes([0xFF]))

    def show_all_registers(self):
        """Read all registers."""
        current_config = self.bus.readfrom_mem(self.address, self.REGISTER_CONFIGURATION,1)
        output_register = self.bus.readfrom_mem(self.address, self.REGISTER_OUTPUT_PORT,1)
        input_register = self.bus.readfrom_mem(self.address, self.REGISTER_INPUT_PORT,1)
        return current_config, output_register, input_register

    def set_pin(self, wbit):
        """Set one of the output pins HIGH."""
        #print("set pin: ", wbit)
        # print("bitwise, the pin is", format((1 << wbit), '#010b'))
        # check that the channel is set to OUTPUT
        current_config = self.bus.readfrom_mem(self.address, self.REGISTER_CONFIGURATION,1)
        if(current_config[0] & (1 << wbit)):
            # bit is set, channel is in INPUT mode
            new_config = current_config[0] & ~(1 << wbit)
            # write new config to TCA95344
            new_configs = new_config.to_bytes(1, 'big')
            self.bus.writeto_mem(self.address, self.REGISTER_CONFIGURATION, new_configs)
        current_outputs = self.bus.readfrom_mem(self.address, self.REGISTER_OUTPUT_PORT,1)
        current_outputs = current_outputs[0] | (1 << wbit)
        updated_outputs = current_outputs.to_bytes(1, 'big')
        self.bus.writeto_mem(self.address, self.REGISTER_OUTPUT_PORT, updated_outputs)

    def clear_pin(self, wbit):
        """Set one of the output pins LOW."""
        #print("clear pin: ", wbit)
        # print("bitwise, the pin is", format((1 << wbit), '#010b'))
        # check that the channel is set to OUTPUT
        current_config = self.bus.readfrom_mem(self.address, self.REGISTER_CONFIGURATION,1)
        if(current_config[0] & (1 << wbit)):
            # bit is set, channel is in INPUT mode
            new_config = current_config[0] | (1 << wbit)
            # write new config to TCA95344
            new_configs = new_config.to_bytes(1, 'big')
            self.bus.writeto_mem(self.address, self.REGISTER_CONFIGURATION, new_configs)
        current_outputs = self.bus.readfrom_mem(self.address, self.REGISTER_OUTPUT_PORT,1)
        #print(f"current_outputs: {current_outputs[0]:08b}")
        current_outputs = current_outputs[0] & ~(1 << wbit)
        updated_outputs = current_outputs.to_bytes(1, 'big')
        self.bus.writeto_mem(self.address, self.REGISTER_OUTPUT_PORT, updated_outputs)

    def write_pin(self, wbit, value):
        """More Arduino-like format for writing a 1 or 0 to a pin."""
        if value:
            self.set_pin(wbit)
        else:
            self.clear_pin(wbit)

    def read_pin(self, wbit):
        """Read one of the pins as INPUT."""
        #print("read pin: ", wbit)
        # print("bitwise, the pin is", format((1 << wbit), '#010b'))
        # check that the channel is set to INPUT
        current_config = self.bus.readfrom_mem(self.address, self.REGISTER_CONFIGURATION,1)
        if(current_config[0] & (1 << wbit)):
            # bit is set, channel is in INPUT mode
            pass
        else:
            # bit is clear, channel is in OUTPUT mode
            new_config = current_config[0] | (1 << wbit)
            #print(f"new config: {new_config:08b}")
            # write new config to TCA95344
            new_configs = new_config.to_bytes(1, 'big')
            self.bus.writeto_mem(self.address, self.REGISTER_CONFIGURATION, new_configs)
        current_inputs = self.bus.readfrom_mem(self.address, self.REGISTER_INPUT_PORT,1)
        #print(f"current_inputs: {current_inputs[0]:08b}")
        isset = current_inputs[0] & (1 << wbit)
        return isset
        #print(f"isset: {isset:08b}")