import PyQt5.QtWidgets as QtWidgets

app = QtWidgets.QApplication([])
dialog = QtWidgets.QDialog()
mass_label = QtWidgets.QLabel('mass', dialog)

mass_edit = QtWidgets.QLineEdit('2.5', dialog)
exit_button = QtWidgets.QPushButton('Exit', dialog)

layout = QtWidgets.QVBoxLayout()
layout.addWidget(mass_label)
layout.addWidget(mass_edit)
layout.addWidget(exit_button)
dialog.setLayout(layout)
dialog.exec()
