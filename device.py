from PyQt5.QtWidgets import QLabel, QGridLayout, QLineEdit, QTextEdit, QPushButton, QWidget


class Device(QWidget):
    def __init__(self, drop_widget, parent=None):
        super(Device, self).__init__(parent)
        self.statement=""
        self.drop_widget = drop_widget
        self.nameLabel = QLabel("Item:")
        self.name=QLineEdit()
        self.addButton = QPushButton("&Add")
        self.addButton.setDefault(True)
        self.addButton.clicked.connect(self.add)

        mainLayout = QGridLayout()
        mainLayout.setSpacing(10)

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        self.titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        self.clearButton = QPushButton('Send', self)


        mainLayout.addWidget(title, 1, 0)
        mainLayout.addWidget(self.titleEdit, 1, 1)

        mainLayout.addWidget(author, 2, 0)
        mainLayout.addWidget(authorEdit, 2, 1)

        mainLayout.addWidget(review, 3, 0)
        mainLayout.addWidget(reviewEdit, 3, 1, 5, 1)

        mainLayout.addWidget(self.clearButton, 9, 1)
        self.clearButton.clicked.connect(self.add)
        """
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.nameLabel, 0, 0)
        mainLayout.addWidget(self.name,0,1)
        mainLayout.addWidget(self.addButton, 0, 3)
        """
        self.setLayout(mainLayout)
        self.setWindowTitle(" Device")
        self.setFixedSize(self.sizeHint())
    def add(self, text):
        name = self.titleEdit.text()
        self.drop_widget.updatestock(name)
        self.titleEdit.clear()