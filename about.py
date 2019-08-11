from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

class About(QWidget):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)

        nameLabel2 = QLabel("About:")
        nameLabelT = QLabel("This is software for automatic data acquisition developed by Py Technologies.")
        nameLabelT.setWordWrap(True)
        nameLabelT.setAlignment(Qt.AlignCenter)
        changeButton = QPushButton("Change")

        self.itemstock=QComboBox(self)
        self.itemstock.activated[str].connect(self.updatestock)
        mainLayout = QGridLayout()
        mainLayout.addWidget(nameLabel2, 0, 0)
        mainLayout.addWidget(self.itemstock, 0, 1)
        mainLayout.addWidget(nameLabelT, 1, 0)
        mainLayout.addWidget(changeButton, 2, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle("About")
        self.setFixedSize(self.sizeHint())

    def updatestock(self,name):
        self.itemstock.addItem(name)

    def checkLicenceKey(self,name):
        self.itemstock.addItem(name)