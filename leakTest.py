from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QGridLayout, QGroupBox, QHBoxLayout, QPushButton, \
    QVBoxLayout, QLineEdit

class LeakTest(QWidget):
    def __init__(self, parent=None):
        super(LeakTest, self).__init__(parent)

        #nameLabel2 = QLabel("Item:")
        #self.itemstock=QComboBox(self)
        #self.itemstock.activated[str].connect(self.updatestock)
        #mainLayout = QGridLayout()
        #mainLayout.addWidget(nameLabel2, 0, 0)
        #mainLayout.addWidget(self.itemstock, 0, 1)
        #self.setLayout(mainLayout)
        self.createVerticalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.setWindowTitle("Settings")
        self.setFixedSize(self.sizeHint())

    def createVerticalLayout(self):
        self.horizontalGroupBox = QGroupBox("Leak Test")
        layout = QGridLayout()

        lastIDLabel = QLabel("Last ID (auto increments)")
        dateFormat = QLabel("Date format (ex: yyyy-MM-dd-HHmmss)")
        reportNameFormat = QLabel("Report name format (use: DATE, ID)")
        reportPath = QLabel("Report path")
        soundAlert = QLabel("Sound alert")
        testTime = QLabel("Test time, sec")
        pressureUnits = QLabel("Pressure units")
        leakRateUnits = QLabel("Leak rate units")

        lastIDLine = QLineEdit()
        lastIDLine.setText("70")
        dateFormatLine = QLineEdit()
        dateFormatLine.setText("yyyy-MM-dd HHmmss")
        reportNameFormatLine = QLineEdit()
        reportNameFormatLine.setText("Report-DATE-ID")
        reportPathLine = QLineEdit()
        reportPathLine.setText("C:\\Users\\Roman\\Desktop")

        soundAlertLine = QComboBox()
        soundAlertLine.addItems({"---", "Sound 1"})
        #soundAlertLine.addItem("---")
        #soundAlertLine.addItem("Sound 1")
        testTimeLine = QLineEdit()
        testTimeLine.setText("120")
        pressureUnitsLine = QLineEdit()
        pressureUnitsLine.setText("bar")
        leakRateUnitsLine = QComboBox()
        #leakRateUnitsLine.addItem("P/min")
        #leakRateUnitsLine.addItem("P/h")
        #leakRateUnitsLine.addItem("P/sec")
        leakRateUnitsLine.addItems({"P/min", "P/h", "P/sec"})

        saveButton = QPushButton('Save', self)
        closeButton = QPushButton('Close', self)

        #buttonBlue.clicked.connect(self.on_click)
        layout.addWidget(lastIDLabel,0,0)
        layout.addWidget(lastIDLine,0,1)

        layout.addWidget(dateFormat, 1, 0)
        layout.addWidget(dateFormatLine,1,1)

        layout.addWidget(reportNameFormat, 2, 0)
        layout.addWidget(reportNameFormatLine, 2, 1)

        layout.addWidget(reportPath, 3, 0)
        layout.addWidget(reportPathLine, 3, 1)

        layout.addWidget(soundAlert, 4, 0)
        layout.addWidget(soundAlertLine, 4, 1)

        layout.addWidget(testTime, 5, 0)
        layout.addWidget(testTimeLine, 5, 1)

        layout.addWidget(pressureUnits, 6, 0)
        layout.addWidget(pressureUnitsLine, 6, 1)

        layout.addWidget(leakRateUnits, 7, 0)
        layout.addWidget(leakRateUnitsLine, 7, 1)

        layout.addWidget(saveButton, 8, 0)
        layout.addWidget(closeButton, 8, 1)
        closeButton.clicked.connect(self.close)

        self.horizontalGroupBox.setLayout(layout)

    def updatestock(self,name):
        self.itemstock.addItem(name)