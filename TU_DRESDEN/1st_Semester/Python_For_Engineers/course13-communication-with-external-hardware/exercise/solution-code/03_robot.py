from ipydex import IPS
from arduino_lib import RobotCommunicator


# Create instance of the corresponding class (pass interface)
# port name: e.g. "COM4" on Windows,  "/dev/ttyUSB0" on Unix
#RC = RobotCommunicator('COM4')
RC = RobotCommunicator("/dev/ttyUSB0")


# call the appropriate methods (check the source code of the class)
RC.forward(200)
RC.sound()
res = RC.read_analog()
print(res)
RC.backward(200)


# start interactive shell
# IPS()
