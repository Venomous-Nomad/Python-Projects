from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import random

class MainWindow(qtw.QWidget):
    def __init__(self):
        self.capitalslist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numberslist = '0123456789'
        self.specialslist = '!@#$%^&*?'
        super().__init__()
        self.resize(300,300)
        self.setWindowTitle('Password Generator')

        self.lengthlabel = qtw.QLabel('Password length')
        self.capitalslabel = qtw.QLabel('Capitals')
        self.numberslabel = qtw.QLabel('Numbers')
        self.specialslabel = qtw.QLabel('Special characters')
        self.length = qtw.QComboBox()
        self.length.addItem('4')
        self.length.addItem('6')
        self.length.addItem('12')
        self.length.addItem('18')
        self.length.addItem('20')
        self.length.addItem('30')
        self.generate = qtw.QPushButton('Generate', clicked=self.generate)
        self.password = qtw.QLineEdit()
        self.capitals = qtw.QCheckBox()
        self.numbers = qtw.QCheckBox()
        self.specials = qtw.QCheckBox()
        
        self.setLayout(qtw.QFormLayout())
        self.layout().addRow(self.lengthlabel, self.length)
        self.layout().addRow(self.capitalslabel, self.capitals)
        self.layout().addRow(self.numberslabel, self.numbers)
        self.layout().addRow(self.specialslabel, self.specials)
        self.layout().addRow(self.generate)
        self.layout().addRow(self.password)
        self.show()

    def generate(self):
        self.word = ''
        self.passlist = 'abcdefghijklmnopqrstuvwxyz'
        self.leng = int(self.length.itemText(self.length.currentIndex()))
        if self.capitals.isChecked():
            self.passlist += self.capitalslist
        if self.numbers.isChecked():
            self.passlist += self.numberslist
        if self.specials.isChecked():
            self.passlist += self.specialslist
        for i in range(self.leng):
            self.word += random.choice(self.passlist)
        self.password.setText(self.word)

app = qtw.QApplication([])
mw = MainWindow()
app.exec()
