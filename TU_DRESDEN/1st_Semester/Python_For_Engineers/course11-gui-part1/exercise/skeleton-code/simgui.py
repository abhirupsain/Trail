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


# QApplication instance is always needed (just accept sys.argv)
app = QtWidgets.QApplication(sys.argv)


# ------------------------------------------------------------------------------


# create dialog window
dialog = QtWidgets.QDialog()


# task 11.1.1
# label and input fields

mass1_label = QtWidgets.QLabel('mass trolley', dialog)
mass1_edit = QtWidgets.QLineEdit('0.8', dialog)

# ...

# task 11.1.2

# ...


# task 11.1.3
# buttons
# exit_button =


# task 11.1.4
# specify layout
layout = QtWidgets.QGridLayout()
# layout.addWidget(...
# ...
dialog.setLayout(layout)


# task 11.1.5
# limit input characters (only float numbers should be allowed)
# ...

# task 11.1.6
# set alignment
# ...


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
    c.set("XXX", "XXX", mass1_edit.text())
    c.XXX


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
    # mass1_edit.setText(...)




def simulate():
    """
    This function reads the parameters from all LineEdits, converts them to
    floats and executes the simulation with them. Afterwards the
    results are displayed with matplotlib.
    The initial values of the simulation are still statically predefined here.
    """

    # fetch values from the gui
    m1 = float(mass1_edit.text())
    # ...

    # create time array
    # t = ...

    # execute simulation (todo: use solve_ivp here) see task description
    # res ...

    # Plot the results
    # Here we have to do some trickery: we create a new dialog on which
    # matplotlib draws. The plotDialog has our main dialog as parent and is 'modeless'.
    # This allows us to plot as many result windows as we want in parallel.

    fig = plt.figure()

    plotDialog = QtWidgets.QDialog(dialog)
    fig.canvas.parent().setParent(plotDialog)

    # result for the trolley
    ax1 = fig.add_subplot(2, 1, 1)
    # ...


    # result for the load
    # ax2 = ...

    # Here now the dialog is displayed and no longer the show function of
    # matplotlib is called
    plot_dialog.show()


# task 11.1.7
# connect button
# simulation_button.clicked.XXX

# task 11.2.1
# ...

#-------------------------------------------------------------------------------

# Show the dialog
dialog.exec_()
