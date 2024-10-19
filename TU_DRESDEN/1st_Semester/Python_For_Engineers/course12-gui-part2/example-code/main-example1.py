import PyQt5.QtWidgets as QtWidgets


class Gui(QtWidgets.QMainWindow):
    """
    Own class (derived from QMainWindow).
    This class (yet) does not do anything.
    """

    def __init__(self):
        # call the "constructor" of the base-class
        QtWidgets.QMainWindow.__init__(self)


app = QtWidgets.QApplication([])

gui = Gui()  # create an instance of the new class
gui.show()
app.exec_()
