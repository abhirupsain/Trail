import PyQt5.QtWidgets as QtWidgets

app = QtWidgets.QApplication([])
dialog = QtWidgets.QDialog()
mass_label = QtWidgets.QLabel('mass', dialog)

# ... like gui-example1.py + two new widgets
mass_edit = QtWidgets.QLineEdit('2.5', dialog)
exit_button = QtWidgets.QPushButton('Exit', dialog)
dialog.exec()
