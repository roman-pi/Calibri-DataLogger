import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class menudemo(QMainWindow):
  def __init__(self, parent=None):
    super(menudemo, self).__init__(parent)

    self.pilot_widget=AddInventory()
    self.drop_widget=AddressBook()

    self.centralWidget=QMdiArea(self)
    self.setCentralWidget(self.centralWidget)

    self.sub1=QMdiSubWindow()
    self.sub1.setWidget(self.drop_widget)
    self.centralWidget.addSubWindow(self.sub1)
    self.sub1.show()

    self.sub2=QMdiSubWindow()
    self.sub2.setWidget(self.pilot_widget)
    self.centralWidget.addSubWindow(self.sub2)
    self.sub2.show()
    self.setWindowTitle("menu demo")
    self.showMaximized()

class AddInventory(QWidget):
 def __init__(self, parent=None):
    super(AddInventory, self).__init__(parent)
    self.statement=""
    self.nameLabel = QLabel("Item:")
    self.name=QLineEdit()
    self.addButton = QPushButton("&Add")
    self.addButton.setDefault(True)
    self.addButton.clicked.connect(self.add)
    mainLayout = QGridLayout()
    mainLayout.addWidget(self.nameLabel, 0, 0)
    mainLayout.addWidget(self.name,0,1)
    mainLayout.addWidget(self.addButton, 0, 3)
    self.setLayout(mainLayout)
    self.setWindowTitle(" Address Book")
    self.setFixedSize(self.sizeHint())
 def add(self,text):
    name=self.name.text()
    AddressBook().updatestock(name)
    self.name.clear()

class AddressBook(QWidget):
 def __init__(self, parent=None):
    super(AddressBook, self).__init__(parent)


    nameLabel2 = QLabel("Item:")
    self.itemstock=QComboBox(self)
    self.itemstock.activated[str].connect(self.updatestock)
    mainLayout = QGridLayout()
    mainLayout.addWidget(nameLabel2, 0, 0)
    mainLayout.addWidget(self.itemstock, 0, 1)
    self.setLayout(mainLayout)
    self.setWindowTitle("Simple Address Book")
    self.setFixedSize(self.sizeHint())

 def updatestock(self,name):
    print(name)
    self.itemstock.addItem(name)

def main():
 app = QApplication(sys.argv)
 ex = menudemo()
 ex.show()
 sys.exit(app.exec_())

if __name__ == '__main__':
 main()