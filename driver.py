from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QGridLayout

class Driver(QWidget):
    def __init__(self, parent=None):
        super(Driver, self).__init__(parent)

        nameLabel2 = QLabel("Item:")
        self.itemstock=QComboBox(self)
        self.itemstock.activated[str].connect(self.updatestock)
        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel2, 0, 0)
        mainLayout.addWidget(self.itemstock, 0, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("Driver")
        self.setFixedSize(self.sizeHint())

    def updatestock(self,name):
        self.itemstock.addItem(name)