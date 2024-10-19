import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore

app = QtWidgets.QApplication([])
dialog = QtWidgets.QDialog()
mass_label = QtWidgets.QLabel('mass', dialog)

mass_edit = QtWidgets.QLineEdit('2.5', dialog)
exit_button = QtWidgets.QPushButton('Exit', dialog)

len_label = QtWidgets.QLabel('pendulum length', dialog)
len_edit = QtWidgets.QLineEdit('1', dialog)

layout = QtWidgets.QGridLayout()
layout.addWidget(mass_label, 0, 0)  # widget, row, column
layout.addWidget(mass_edit, 0, 1)
layout.addWidget(len_label, 1, 0)
layout.addWidget(len_edit, 1, 1)
layout.addWidget(exit_button, 2, 1, QtCore.Qt.AlignRight)
dialog.setLayout(layout)
dialog.exec() # run dialog for the first time

m = float(mass_edit.text())
# write text to command line
print("mass input in the dialog:", m)

mass_edit.setText(str(m*2))
dialog.exec() # run dialog for the second time
