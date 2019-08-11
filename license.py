from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt

class License(QWidget):
    def __init__(self, parent=None):
        super(License, self).__init__(parent)

        nameLabel2 = QLabel("Accepted")
        nameLabel2.setAlignment(Qt.AlignCenter)

        nameLabelT = QLabel("This is software for automatic data acquisition developed by Py Technologies.")
        nameLabelT.setWordWrap(True)
        nameLabelT.setAlignment(Qt.AlignCenter)
        licenseKey = QLineEdit()
        licenseKey.setStyleSheet("color: green")
        licenseKey.setInputMask('>NNNNN-NNNNN-NNNNN-NNNNN-NNNNN;#')
        licenseKey.setAlignment(Qt.AlignCenter)
        changeButton = QPushButton("Change")


        mainLayout = QGridLayout()

        mainLayout.addWidget(nameLabelT, 1, 0)
        mainLayout.addWidget(changeButton, 4, 0)
        mainLayout.addWidget(licenseKey, 2, 0)
        self.setLayout(mainLayout)
        self.setWindowTitle("License")
        self.setFixedSize(self.sizeHint())

    def updatestock(self,name):
        self.itemstock.addItem(name)

    def checkLicenceKey(self,name):
        self.itemstock.addItem(name)