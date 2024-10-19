import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore

import configparser as cfg

from ipydex import IPS


class NumberInput(QtWidgets.QWidget):
    """
    Widget, which contains two subwidgets : a label for description and a LineEdit for input.
    The two widgets are arranged in a horizontal layout.
    Values are automatically converted between QString and float when using the functions
    `setValue` and `getValue`.
    """

    def __init__(self, text, value=0, parent=None):

        # call the "constructor" of the base-class
        QtWidgets.QWidget.__init__(self, parent)

        # create the two sub widgets
        self.label = QtWidgets.QLabel(parent)

        self.edit = QtWidgets.QLineEdit(parent)
        self.edit.setAlignment(QtCore.Qt.AlignRight)
        self.edit.setValidator(QtGui.QDoubleValidator(self.edit))

        # set values (arguments passed to the constructor)
        self.setText(text)
        self.setValue(value)

        # create and set layout
        self.hBox = QtWidgets.QHBoxLayout()
        # self.hBox.setMargin(5)
        self.hBox.addWidget(self.label)
        self.hBox.addStretch(1.0)
        self.hBox.addWidget(self.edit)

        self.setLayout(self.hBox)

        # limit the maximum width of the input field (optics)
        self.edit.setMaximumWidth(70)

    def setText(self, text):
        """
        set label text
        """

        if not isinstance(text, str):
            raise TypeError(f"Argument `text` must be of type `str`. Got {type(text)} instead.")

        self.label.setText(text)

    def getText(self):
        """
        return the label text as python string
        """

        return str(self.label.text())

    def setValue(self, value):
        """
        Set the value of the input field, expects a number as argument
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Argument `value` must be a real number. Got {type(text)} instead.")

        self.edit.setText(str(value))

    def getValue(self):
        """
        return value of the input field as float
        """

        return float(str(self.edit.text()))

    # create two 'properties' for convenient access to the internal attributes
    # like 'decorators' (see course 7) 'properties' are an advanced python technique
    # see https://docs.python.org/3/library/functions.html#property
    value = property(getValue, setValue)
    text = property(getText, setText)

    # end of class NumberInput


class ParameterMask(QtWidgets.QWidget):
    """
    Encapsulation of all input fields in one widget. It provides at the same time
    functions for saving and loading parameters in a configuration file.
    file.
    """

    def __init__(self, parent=None):

        # call the "constructor" of the base-class
        QtWidgets.QWidget.__init__(self, parent)

        # widgets for parameter input
        self.m_trolley = NumberInput("trolley mass", 10, self)
        self.m_load = NumberInput("load mass", 2.5, self)
        self.dt = NumberInput("step size", 0.02, self)
        self.tEnd = NumberInput("simulation duration", 10, self)

        # layout
        self.vBox = QtWidgets.QVBoxLayout()
        self.vBox.addWidget(self.m_trolley)
        self.vBox.addWidget(self.m_load)
        self.vBox.addWidget(self.dt)
        self.vBox.addWidget(self.tEnd)
        self.vBox.addStretch(1.0)
        # self.vBox.setMargin(0)

        self.setLayout(self.vBox)

        # limit maximum width
        self.setMaximumWidth(200)

    def openfile(self):
        """
        Open an `.ini` file and read the stored data
        """

        # dialog for opening a file
        fName, _filter = QtWidgets.QFileDialog.getOpenFileName(filter="*.ini")

        if not fName:
            return

        # create config parser
        c = cfg.SafeConfigParser()

        # read from file
        if c.read(fName):
            print(f"{fName} successfully loaded")
        else:
            print("no configuration file loaded")

        # read parmeters
        self._readparams(c, "Parameter", [self.m_trolley, self.m_load])
        self._readparams(c, "Simulation", [self.dt, self.tEnd])

    def _readparams(self, cfgParser, section, paramList):
        """
        This function is only needed to add error handling for the parameter reading.

        :param cfgParser:   ConfigParser instance
        :param section:     str; specifying the section to read from
        :param paramList:   list; list of the input fields to be filled


        The function checks if the section exists in the file at all and sets all values to one
        if it does not exist. The advantage of the detailed error handling is that most parameters
        continue to be read in correctly even if a value or a section is missing.
        """

        # chec if section exists
        try:
            cfgParser.get(section, "")
        except cfg.NoSectionError:
            msg = "Section '{}' does not exist in configuration file. Set all parameters all to 1."
            print(msg.format(section))

            for p in paramList:
                p.value = 1
            return
        except cfg.NoOptionError:
            pass

        # Lesen der Parameter
        for i in paramList:
            try:
                i.value = float(cfgParser.get(section, i.text))

            except cfg.NoOptionError:
                msg = "Parameter '{0}' does not exist in config file. Setting '{0}':=1."
                print(msg.format(i.text))
                i.value = 1


    def savefile(self):
        """
        Open dialog to select a file and save current parameters in it
        """

        # Dialog für Dateiname
        fName, _filter = QtWidgets.QFileDialog.getSaveFileName(filter="*.ini")

        if not fName:
            return

        # create Configparser instance and pass data
        c = cfg.ConfigParser()

        c.add_section("Parameter")
        c.set("Parameter", self.m_trolley.text, str(self.m_trolley.value))
        c.set("Parameter", self.m_load.text, str(self.m_load.value))

        c.add_section("Simulation")
        c.set("Simulation", self.dt.text, str(self.dt.value))
        c.set("Simulation", self.tEnd.text, str(self.tEnd.value))

        # write config file
        with open(fName, "w") as fid:
            c.write(fid)

    # end of class ParameterMask


class IVSlider(QtWidgets.QWidget):
    """
    'Initial Value Slider'
    Label and slider to change the initial values of the simulation, arranged in horizontal layout.
    """

    def __init__(self, text, limits, parent=None):
        """
        Constructor

        :param text:    str; label of the slider
        :param limits:  list or tuple of length 2; min und max value of the slider (int values)
        """

        # call the constructor of the base class
        QtWidgets.QWidget.__init__(self, parent)

        # label und slider
        self.label = QtWidgets.QLabel(text)
        self.slider = QtWidgets.QSlider()

        # limits of the slider - caution: nur int values are accepted
        self.slider.setMinimum(limits[0])
        self.slider.setMaximum(limits[1])

        # slider orientation
        self.slider.setOrientation(QtCore.Qt.Horizontal)

        # layout
        self.hBox = QtWidgets.QHBoxLayout()
        self.hBox.addWidget(self.label)
        self.hBox.addWidget(self.slider)

        self.setLayout(self.hBox)

        # adapt size
        self.label.setFixedWidth(20)
        self.setMaximumWidth(200)

    def getValue(self):
        """
        return the value of the slider as float
        """

        return float(self.slider.value())

    # end of class IVSlider
