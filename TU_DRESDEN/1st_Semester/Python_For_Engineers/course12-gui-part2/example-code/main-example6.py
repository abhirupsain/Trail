import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore


class Gui(QtWidgets.QMainWindow):
    """
    Own class (derived from QMainWindow).
    This class (yet) does not do much.
    """

    def __init__(self):
        # call the "constructor" of the base-class
        QtWidgets.QMainWindow.__init__(self)

        # self.menuBar is a method of the base class
        self.menu_file = self.menuBar().addMenu("&File")
        self.menu_recent = self.menu_file.addMenu("Recently opened ...")

        self.act_exit = QtWidgets.QAction(self)
        self.act_exit.setText("Quit")
        self.act_exit.setIcon(QtGui.QIcon("../exercise/data/exit.png"))
        self.act_exit.setShortcut("Ctrl+Q")
        self.menu_file.addAction(self.act_exit)

        self.act_exit.triggered.connect(self.close)

        self.toolbar = QtWidgets.QToolBar("File")
        self.toolbar.setIconSize(QtCore.QSize(24, 24))
        self.addToolBar(self.toolbar)

        self.toolbar.addAction(self.act_exit)

        self.cw = QtWidgets.QWidget()
        self.setCentralWidget(self.cw)

        self.vBox = QtWidgets.QVBoxLayout(self.cw)

        self.label = QtWidgets.QLabel("Click me with right mouse button!")
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.addAction(self.act_exit)

        self.vBox.addWidget(self.label)

        self.slider = QtWidgets.QSlider(self)
        self.slider.setMinimum(-10)
        self.slider.setMaximum(10)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.vBox.addWidget(self.slider)

        self.slider.valueChanged.connect(self.label.setNum)
        self.slider.valueChanged.connect(self.print_value)

    def print_value(self, x):
        print(x)


app = QtWidgets.QApplication([])

gui = Gui()  # create an instance of the new class
gui.show()
app.exec_()
