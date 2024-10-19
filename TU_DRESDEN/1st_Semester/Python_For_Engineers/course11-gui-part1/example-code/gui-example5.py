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

mass_edit.setAlignment(QtCore.Qt.AlignRight)
len_edit.setAlignment(QtCore.Qt.AlignRight)

def openfile():
    path, type_filter = QtWidgets.QFileDialog.getOpenFileName()
    print(path, type_filter)

def savefile():
    path, type_filter = QtWidgets.QFileDialog.getSaveFileName()
    print(path, type_filter)

open_button = QtWidgets.QPushButton('Open', dialog)
save_button = QtWidgets.QPushButton('Save', dialog)

layout.addWidget(open_button, 3, 1, QtCore.Qt.AlignRight)
layout.addWidget(save_button, 4, 1, QtCore.Qt.AlignRight)

open_button.clicked.connect(openfile)
save_button.clicked.connect(savefile)
exit_button.clicked.connect(dialog.close)

dialog.setLayout(layout)
dialog.exec()
