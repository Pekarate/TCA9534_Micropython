"""Interface with the Qwiic GPIO board, a TCA9534 I/O expander.

Set and read 8 digitalchannels.
TCA9534 datasheet:
https://www.ti.com/lit/ds/symlink/tca9534.pdf
QWIIC GPIO board:
https://github.com/sparkfunX/Qwiic_GPIO

by aka.farm 09/2020
"""
import smbus


class TCA9534:
    """Instance of TCA9534 I/O expander."""

    REGISTER_INPUT_PORT = 0x00    # register 0
    REGISTER_OUTPUT_PORT = 0X01    # register 1
    REGISTER_CONFIGURATION = 0X03    # register 3

    def __init__(self, i2c_ch=1, tca9534_address=0x27, output=True, bitmask=None):
        """Default values taken from Sparkfun QWIIC GPIO board."""
        self.address = tca9534_address
        self.bus = smbus.SMBus(i2c_ch)
        if bitmask:
            self.bus.write_byte_data(self.address, self.REGISTER_CONFIGURATION, bitmask)
            print("set bitmask: ", format(self.bus.read_byte_data(self.address, self.REGISTER_CONFIGURATION)))
            return
        print("no bitmask, setting up all channels")
        if output:
            # set all 8 channels to OUTPUT by writing 0
            print("...for write")
            self.bus.write_byte_data(self.address, self.REGISTER_CONFIGURATION, 0b00000000)
            self.bus.write_byte_data(self.address, self.REGISTER_OUTPUT_PORT, 0b00000000)
        else:
            # set all 8 channels to INPUT by writing 1
            print("...for read")
            self.bus.write_byte_data(self.address, self.REGISTER_CONFIGURATION, 0b11111111)

    def show_all_registers(self):
        """Read all registers."""
        current_config = self.bus.read_byte_data(self.address, self.REGISTER_CONFIGURATION)
        output_register = self.bus.read_byte_data(self.address, self.REGISTER_OUTPUT_PORT)
        input_register = self.bus.read_byte_data(self.address, self.REGISTER_INPUT_PORT)
        print("configuration register: ", format(current_config, '#010b'))
        print("output register: ", format(output_register, '#010b'))
        print("input register: ", format(input_register, '#010b'))
        return

    def set_pin(self, wbit):
        """Set one of the output pins HIGH."""
        print("set pin: ", wbit)
        # print("bitwise, the pin is", format((1 << wbit), '#010b'))
        # check that the channel is set to OUTPUT
        current_config = self.bus.read_byte_data(self.address, self.REGISTER_CONFIGURATION)
        if(current_config & (1 << wbit)):
            # bit is set, channel is in INPUT mode
            new_config = current_config | (1 << wbit)
            print("need to set this channel to OUTPUT, new config: ", format(new_config, '#010b'))
            # write new config to TCA95344
            self.bus.write_byte_data(self.address, self.REGISTER_CONFIGURATION, new_config)
        current_outputs = self.bus.read_byte_data(self.address, self.REGISTER_OUTPUT_PORT)
        print("current_outputs: ", format(current_outputs, '#010b'))
        current_outputs |= (1 << wbit)
        self.bus.write_byte_data(self.address, self.REGISTER_OUTPUT_PORT, current_outputs)
        print("updated current_outputs: ", format(self.bus.read_byte_data(self.address, self.REGISTER_OUTPUT_PORT), '#010b'))

    def clear_pin(self, wbit):
        """Set one of the output pins LOW."""
        print("clear pin: ", wbit)
        # print("bitwise, the pin is", format((1 << wbit), '#010b'))
        # check that the channel is set to OUTPUT
        current_config = self.bus.read_byte_data(self.address, self.REGISTER_CONFIGURATION)
        if(current_config & (1 << wbit)):
            # bit is set, channel is in INPUT mode
            new_config = current_config | (1 << wbit)
            print("need to set this channel to OUTPUT, new config: ", format(new_config))
            # write new config to TCA95344
            self.bus.write_byte_data(self.address, self.REGISTER_CONFIGURATION, new_config)
        current_outputs = self.bus.read_byte_data(self.address, self.REGISTER_OUTPUT_PORT)
        print("current_outputs: ", format(current_outputs, '#010b'))
        current_outputs &= ~(1 << wbit)
        self.bus.write_byte_data(self.address, self.REGISTER_OUTPUT_PORT, current_outputs)
        print("updated current_outputs: ", format(self.bus.read_byte_data(self.address, self.REGISTER_OUTPUT_PORT), '#010b'))

    def read_pin(self, wbit):
        """Read one of the pins as INPUT."""
        print("read pin: ", wbit)
        # print("bitwise, the pin is", format((1 << wbit), '#010b'))
        # check that the channel is set to INPUT
        current_config = self.bus.read_byte_data(self.address, self.REGISTER_CONFIGURATION)
        if(current_config & (1 << wbit)):
            # bit is set, channel is in INPUT mode
            pass
        else:
            # bit is clear, channel is in OUTPUT mode
            new_config = current_config | (1 << wbit)
            print("new config ", format(new_config, '#010b'))
            # write new config to TCA95344
            self.bus.write_byte_data(self.address, self.REGISTER_CONFIGURATION, new_config)
        current_inputs = self.bus.read_byte_data(self.address, self.REGISTER_INPUT_PORT)
        print("current_inputs: ", format(current_inputs, '#010b'))
        isset = format(current_inputs & (1 << wbit), '#010b')
        print("isset ", isset)
