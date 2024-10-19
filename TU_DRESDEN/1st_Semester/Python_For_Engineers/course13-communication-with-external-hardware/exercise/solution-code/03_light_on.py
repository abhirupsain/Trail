from ipydex import IPS
from arduino_lib import ArduinoCommunicator


# Create instance of the corresponding class (pass interface)
# port name: e.g. "COM4" on Windows,  "/dev/ttyUSB0" on Unix
#AC = ArduinoCommunicator("COM4")
AC = ArduinoCommunicator("/dev/ttyUSB0")


# call the appropriate method (check the source code of the class)
AC.light_on(30)


# start interactive shell
IPS()
