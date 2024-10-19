"""
Communication with the mobile robot via serial interface
(emulated via USB)

"""

from numpy import clip
from ipydex import IPS

import serial
import time


"""
Basic idea: one sends commands of fixed length (2-byte):
first byte: command
second byte: data
"""


class ArduinoCommunicator(object):



    def __init__(self, port = 0, baudrate = 9600, timeout=1):

        self.ser = serial.Serial(port, baudrate, timeout=timeout)

        self._test_communication()  # check consistency


    def _test_communication(self, output = True):
        # generate random bytes between 65 (A) and 122 (z)
        rand_value = int((time.time()*100) %58 + 65)
        rand_byte = self._number_to_byte(rand_value)
        response = self._send("I"+rand_byte)

        if output == False:
            return

        if response.decode("utf8") == rand_byte:
            print("-> Communication established successfully")
        else:
            print("Invalid initialization of serial communication")
            self.ser.flushInput()


    def _send(self, cmd, nores=False):
        """
        internal method for sending
        """

        assert len(cmd) == 2
        # add newline as last byte
        b_cmd = bytes(cmd+"\n", "utf8")
        self.ser.write(b_cmd)

        if nores == True:
            response = ""
        else:
            response = self.ser.readline()[:-1]  # cancel the trailing "\n"

        print("cmd:     ", repr(cmd))
        print("response:", repr(response))

        return response

    def _number_to_byte(self, x, min = 0, max = 255):
        """
        internal method for conversion
        """
        x2 = clip(int(x), min, max)
        if x!=x2:
            print("Invalid value: %s! Instead using: %s" %(str(x), str(x2)))

        print(":::",x, x2, chr(x2))
        return chr(x2)

    def close(self):
        self.ser.close()

    def __del__(self):
        # close port if object is deleted
        self.ser.close()


    def light_on(self, duration):
        """
        light up the LED
        duration in deci seconds
        """
        cmd = "L"+self._number_to_byte(duration)
        self._send(cmd)

        # no return value


class RobotCommunicator(ArduinoCommunicator):
    """
    RobotCommunicator is a subclass of ArduinoCommunicator
    """

    # abstraction layer to have all byte commands in one place:

    commands = {
        "forward": "F",
        "backward": "B",
        "sound": "S",
        "init": "I"
    }

    def forward(self, x):
        databyte = self._number_to_byte(x)
        response = self._send(self.commands["forward"]+databyte)


    def backward(self, x):
        databyte = self._number_to_byte(x)
        response = self._send(self.commands["backward"]+databyte)

    def sound(self):
        # sound command does not receive any data
        self._send(self.commands["sound"]+" ", nores=True)
        time.sleep(1.2)
        self.ser.flushInput()
        self._test_communication(output=False)


    def read_analog(self):
        cmd = "R "
        res = self._send(cmd)

        return res



