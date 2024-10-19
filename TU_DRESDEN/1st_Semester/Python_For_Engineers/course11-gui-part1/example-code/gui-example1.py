import PyQt5.QtWidgets as QtWidgets

app = QtWidgets.QApplication([])
dialog = QtWidgets.QDialog()
mass_label = QtWidgets.QLabel('mass', dialog)
dialog.exec()
