"""
Communication with digital multimeter
"""

from ipydex import IPS
import serial

# port name: e.g. "COM4" on Windows,  "/dev/ttyUSB0" on Unix
s = serial.Serial('COM4')

# Background info: command reference in the device documentation
# SCPI ("Standard Commands for Programmable Instruments")


# ask the device for its ID
s.write("*IDN?\n")
print(s.readline())


# display possible errors
s.write("SYST:ERR?\n")
print(s.readline())


cmd1 = "SYST:REM\n"  # configure (set) mode to 'remote'
cmd2 = "MEAS:VOLT:DC? 10, 0.003\n"


# transfer commands and query result

s.write(cmd1)
s.write(cmd2)
res =  s.readline()

res = float (res)  # convert from string to float
print("Voltage: %s V" % res)


s.close()
