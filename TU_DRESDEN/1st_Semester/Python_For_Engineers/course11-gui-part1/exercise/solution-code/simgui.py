"""
This is the main program.
"""

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

import sys

from model import rhs
from scipy.integrate import odeint
from numpy import arange

import matplotlib
matplotlib.use('Qt5Agg')  # explicitly define Qt backend for matplotlib

import matplotlib.pyplot as plt

import configparser


# QApplication instance is always needed (just accept sys.argv)
app = QtWidgets.QApplication(sys.argv)


# ------------------------------------------------------------------------------


# create dialog window
dialog = QtWidgets.QDialog()


# task 11.1.1
# label and input fields

mass1_label = QtWidgets.QLabel('mass trolley', dialog)
mass1_edit = QtWidgets.QLineEdit('0.8', dialog)

length_label = QtWidgets.QLabel('pendulum length', dialog)
length_edit = QtWidgets.QLineEdit('1.2', dialog)

mass2_label = QtWidgets.QLabel('mass pendulum load', dialog)
mass2_edit = QtWidgets.QLineEdit('0.5', dialog)


# task 11.1.2
step_size_label = QtWidgets.QLabel('simulation step size', dialog)
step_size_edit = QtWidgets.QLineEdit('0.01', dialog)

duration_label = QtWidgets.QLabel('simulation duration', dialog)
duration_edit = QtWidgets.QLineEdit('10.0', dialog)


# task 11.1.3
# buttons
exit_button = QtWidgets.QPushButton('Exit', dialog)
simulation_button = QtWidgets.QPushButton('Simulate', dialog)

exit_button.clicked.connect(dialog.close)


# task 11.1.4
# specify layout
layout = QtWidgets.QGridLayout()
layout.addWidget(length_label, 0, 0)  # widget, row, column
layout.addWidget(length_edit, 0, 1)
layout.addWidget(mass1_label, 1, 0)
layout.addWidget(mass1_edit, 1, 1)
layout.addWidget(mass2_label, 2, 0)
layout.addWidget(mass2_edit, 2, 1)
layout.addWidget(step_size_label, 3, 0)
layout.addWidget(step_size_edit, 3, 1)
layout.addWidget(duration_label, 4, 0)
layout.addWidget(duration_edit, 4, 1)

layout.addWidget(simulation_button, 5, 1, QtCore.Qt.AlignRight)
layout.addWidget(exit_button, 6, 1, QtCore.Qt.AlignRight)

dialog.setLayout(layout)


# task 11.1.5
# limit input characters (only float numbers should be allowed)
length_edit.setValidator(QtGui.QDoubleValidator(length_edit))
mass1_edit.setValidator(QtGui.QDoubleValidator(mass1_edit))
mass2_edit.setValidator(QtGui.QDoubleValidator(mass2_edit))
step_size_edit.setValidator(QtGui.QDoubleValidator(step_size_edit))
duration_edit.setValidator(QtGui.QDoubleValidator(duration_edit))


# task 11.1.6
# set alignment
length_edit.setAlignment(QtCore.Qt.AlignRight)
mass1_edit.setAlignment(QtCore.Qt.AlignRight)
mass2_edit.setAlignment(QtCore.Qt.AlignRight)
step_size_edit.setAlignment(QtCore.Qt.AlignRight)
duration_edit.setAlignment(QtCore.Qt.AlignRight)


# optional: set focus to the exit button
# exit_button.setFocus()


# task 11.1.7

# define the necessary functions
def saveFile():
    """
    Open dialog for selecting a file and save current parameters in it.
    """

    # dialog for filename (returns a 2-tuple), see slide 9
    filename, type_filter = QtWidgets.QFileDialog.getSaveFileName()

    if filename == "":
        return  # if 'cancel' was pressed -> do nothing

    # Create ConfigParser and pass data
    c = configparser.ConfigParser()

    c.add_section('Parameter')
    c.set('Parameter', 'm1', str(mass1_edit.text()))
    c.set('Parameter', 'm2', str(mass2_edit.text()))
    c.set('Parameter', 'l',  str(duration_edit.text()))

    c.add_section('Simulation')
    c.set('Simulation', 'dt', str(step_size_edit.text()))
    c.set('Simulation', 't_end', str(duration_edit.text()))

    # write config file
    with open(filename, 'w') as fid:
        c.write(fid)


def openFile():
    """
    Opens an `.ini` file and reads its data.
    """

    # dialog for filename (returns a 2-tuple), see slide 9
    filename, type_filter = QtWidgets.QFileDialog.getOpenFileName()

    if filename == "":
        return  # if 'cancel' was pressed -> do nothing

    # Create ConfigParser and pass data
    c = configparser.ConfigParser()

    # read from file
    print("loading", filename)

    if c.read(str(filename)):
        print('OK')
    else:
        print("No configuration file loaded")

    # pass values to the according LineEdit instances
    mass1_edit.setText(c.get('Parameter', 'm1'))
    mass2_edit.setText(c.get('Parameter', 'm2'))
    duration_edit.setText(c.get('Parameter', 'l'))

    step_size_edit.setText(c.get('Simulation', 'dx'))
    duration_edit.setText(c.get('Simulation', 't_end'))


def simulate():
    """
    This function reads the parameters from all LineEdits, converts them to
    floats and executes the simulation with them. Afterwards the
    results are displayed with matplotlib.
    The initial values of the simulation are still statically predefined here.
    """

    # fetch values from the gui
    m1 = float(mass1_edit.text())
    m2 = float(mass2_edit.text())
    l = float(duration_edit.text())
    dx = float(step_size_edit.text())
    t_end = float(duration_edit.text())

    # alternatively:
    # m1 = mass1_edit.text().toDouble()[0]   # returns tuple like (value, OK)

    # create time array
    t = arange(0, t_end, dx)

    # execute simulation (todo: use solve_ivp here)
    res = odeint(rhs, [0, 0.3, 0, 0], t, args=(m1, m2, l))

    # Plot the results
    # Here we have to do some trickery: we create a new dialog on which
    # matplotlib draws. The plotDialog has our main dialog as parent and is 'modeless'.
    # This allows us to plot as many result windows as we want in parallel.

    fig = plt.figure()

    plotDialog = QtWidgets.QDialog(dialog)
    fig.canvas.parent().setParent(plotDialog)

    # result for the trolley
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(t, res[:, 0], label='x')
    ax1.plot(t, res[:, 2], label='dx')

    ax1.grid(True)
    ax1.legend()
    ax1.set_ylabel('trolley')

    # result for the load
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(t, res[:, 1], label=r"$\varphi$")
    ax2.plot(t, res[:, 3], label=r"$\dot \varphi$")

    ax2.grid(True)
    ax2.legend()
    ax2.set_xlabel('time [s]')
    ax2.set_ylabel('load')

    # Here now the dialog is displayed and no longer the show function of
    # matplotlib is called
    plotDialog.show()


# task 11.1.7
# connect button
simulation_button.clicked.connect(simulate)

# task 11.2.1

open_button = QtWidgets.QPushButton('Open', dialog)
save_button = QtWidgets.QPushButton('Save', dialog)

open_button.clicked.connect(openFile)
save_button.clicked.connect(saveFile)

layout.addWidget(open_button, 7, 1, QtCore.Qt.AlignRight)
layout.addWidget(save_button, 8, 1, QtCore.Qt.AlignRight)


#-------------------------------------------------------------------------------

# Show the dialog
dialog.exec_()
