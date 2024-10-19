import PyQt5.QtWidgets as QtWidgets


class Gui(QtWidgets.QMainWindow):
    """
    Own class (derived from QMainWindow).
    This class (yet) does not do anything.
    """

    def __init__(self):
        # call the "constructor" of the base-class
        QtWidgets.QMainWindow.__init__(self)

        # self.menuBar is a method of the base class
        self.menu_file = self.menuBar().addMenu("&File")
        
        self.menu_recent = self.menu_file.addMenu("Recently opened ...")


app = QtWidgets.QApplication([])

gui = Gui()  # create an instance of the new class
gui.show()
app.exec_()
