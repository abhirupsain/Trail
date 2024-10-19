import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore


class Gui(QtWidgets.QMainWindow):
    """
    Own class (derived from QMainWindow).
    This class (yet) does do something.
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


app = QtWidgets.QApplication([])

gui = Gui()  # create an instance of the new class
gui.show()
app.exec_()
