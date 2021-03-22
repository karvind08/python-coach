#pip install PyQt5
#pip freeze
#touch hello.py

#pip install pyqt5-tools

import PyQt5.QtWidgets as qtw
#from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		# add title
		self.setWindowTitle('Hello World')
		# set vertical layout
		self.setLayout(qtw.QVBoxLayout())
		#self.setLayout(qtw.QHBoxLayout())
		#label
		my_label = qtw.QLabel('Hello How are you? ')
		# change the font size of label
		my_label.setFont(qtg.QFont('helvetica',20))
		self.layout().addWidget(my_label)

		# create an entry box
		my_entry = qtw.QLineEdit()
		my_entry.setObjectName('Name')
		my_entry.setText('')
		self.layout().addWidget(my_entry)

		#create button
		my_button = qtw.QPushButton('Click Me',clicked = lambda:press_it())
		self.layout().addWidget(my_button)

		# show the app
		self.show()

		def press_it():
			# add name to label
			my_label.setText(f'Hello  {my_entry.text()}')
			# clear the entry box
			my_entry.setText('')

app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()

