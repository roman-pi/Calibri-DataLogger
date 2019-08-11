import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QDesktopWidget, QAction, QMainWindow, \
    QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QTextEdit, QSystemTrayIcon, \
    QColorDialog, QMenu, QMenuBar, QComboBox, QMdiArea, QMdiSubWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from about import About
from device import Device
from driver import Driver
from settings import Settings
from leakTest import LeakTest
from diagram import Diagram
from license import License
from dwt import DWT

class Calibri(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Calibri DataLogger'
        self.width = 800
        self.height = 600

        self.initUI()

        self.createActions()
        self.createTrayIcon()

        self.trayIcon.show()


    def initUI(self):
        self.driver_widget = Driver()
        self.device_widget = Device(self.driver_widget)
        self.about_widget = About()
        self.settings_widget = Settings()
        self.leakTest_widget = LeakTest()
        self.diagram_widget = Diagram()
        self.license_widget = License()
        self.dwt_widget = DWT(self.driver_widget)

        self.centralWidget = QMdiArea(self)
        self.setCentralWidget(self.centralWidget)

        self.sub1 = QMdiSubWindow()
        self.sub1.setWidget(self.driver_widget)
        self.centralWidget.addSubWindow(self.sub1)
        self.sub1.show()

        self.sub2 = QMdiSubWindow()
        self.sub2.setWidget(self.device_widget)
        self.centralWidget.addSubWindow(self.sub2)
        self.sub2.show()
        self.setWindowTitle("menu demo")
        self.showMaximized()

        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        qtRectangle = self.frameGeometry()

        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('File')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')

        saveButton = QAction('Save last configuration ...', self)
        saveButton.setShortcut('Ctrl+S')
        saveButton.triggered.connect(self.connectDevice)
        fileMenu.addAction(saveButton)

        loadButton = QAction('Load last configuration ...', self)
        loadButton.setShortcut('Ctrl+L')
        loadButton.triggered.connect(self.connectDevice)
        fileMenu.addAction(loadButton)

        connectButton = QAction('Connect to ...', self)
        connectButton.setShortcut('Ctrl+C')
        #connectButton.setStatusTip('Connect device')
        connectButton.triggered.connect(self.connectDevice)
        fileMenu.addAction(connectButton)

        disconnectButton = QAction('Disconnect all', self)
        disconnectButton.setShortcut('Ctrl+D')
        #connectButton.setStatusTip('Connect device')
        disconnectButton.triggered.connect(self.disconnectAll)
        fileMenu.addAction(disconnectButton)

        fileMenu.addSeparator()

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        diagramButton = QAction('Show diagram', self)
        diagramButton.triggered.connect(self.openDiagram)
        viewMenu.addAction(diagramButton)

        leakTestButton = QAction('Leak test...', self)
        leakTestButton.triggered.connect(self.openLeakTest)
        viewMenu.addAction(leakTestButton)

        settingsButton = QAction('Settings', self)
        settingsButton.triggered.connect(self.openSettings)
        viewMenu.addAction(settingsButton)

        dwtButton = QAction('DWT', self)
        dwtButton.triggered.connect(self.openDWT)
        viewMenu.addAction(dwtButton)
        """
        helpButton = QAction(QIcon('icon.png'), 'Help', self)
        helpButton.setShortcut('Ctrl+H')
        helpButton.setStatusTip('Help')
        helpButton.triggered.connect(self.close)
        helpMenu.addAction(helpButton)
        """
        aboutButton = QAction(QIcon('icon.png'), 'About program', self)
        aboutButton.setShortcut('Ctrl+A')
        aboutButton.setStatusTip('About program')
        aboutButton.triggered.connect(self.openAbout)
        helpMenu.addAction(aboutButton)

        licenseButton = QAction(QIcon('icon.png'), 'Licence info', self)
        licenseButton.setShortcut('Ctrol+L')
        licenseButton.setStatusTip('License inforamation')
        licenseButton.triggered.connect(self.openLicense)
        helpMenu.addAction(licenseButton)

        self.statusBar().showMessage('DPI620 connected; PACE1000 connected')

        """
        wid = QWidget(self)
        self.setCentralWidget(wid)


        grid = QGridLayout()
        grid.setSpacing(10)
        wid.setLayout(grid)

        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        clearButton = QPushButton('Send', self)


        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        grid.addWidget(clearButton, 9, 1)
        """

        # button.move(self.frameGeometry().width()-110, self.frameGeometry().height()-50)
        self.setGeometry(0, 0, 800, 600)
        qtRectangle = self.frameGeometry()

        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.setWindowTitle('Calibri')
        #self.setWindowIcon(QIcon('plus.gif'))
        self.show()

    def connectDevice(self):
        print("connected")

    def disconnectAll(self):
        print("disconnect all")
        #self.centralWidget.removeSubWindow(self.settings_sub)

        self.centralWidget.removeSubWindow(self.settings_sub)
        self.centralWidget.removeSubWindow(self.about_sub)
        self.centralWidget.removeSubWindow(self.leakTest_sub)
        self.centralWidget.removeSubWindow(self.diagram_sub)


    def openAbout(self):
        self.about_sub = QMdiSubWindow()
        self.about_sub.setWidget(self.about_widget)
        self.centralWidget.addSubWindow(self.about_sub)
        self.about_sub.show()

    def openSettings(self):
        self.settings_sub = QMdiSubWindow()
        self.settings_sub.setWidget(self.settings_widget)
        self.centralWidget.addSubWindow(self.settings_sub)
        self.settings_sub.show()

    def openLeakTest(self):
        self.leakTest_sub = QMdiSubWindow()
        self.leakTest_sub.setWidget(self.leakTest_widget)
        self.centralWidget.addSubWindow(self.leakTest_sub)
        self.leakTest_sub.show()

    def openDiagram(self):
        self.diagram_sub = QMdiSubWindow()
        self.diagram_sub.setWidget(self.leakTest_widget)
        self.centralWidget.addSubWindow(self.leakTest_sub)
        self.leakTest_sub.show()

    def openLicense(self):
        self.license_sub = QMdiSubWindow()
        self.license_sub.setWidget(self.license_widget)
        self.centralWidget.addSubWindow(self.license_sub)
        self.license_sub.show()

    def openDWT(self):
        self.dwt_sub = QMdiSubWindow()
        self.dwt_sub.setWidget(self.dwt_widget)
        self.centralWidget.addSubWindow(self.dwt_sub)
        self.dwt_sub.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

    def closeEvent(self, event):
        buttonReply = QMessageBox.question(self, 'Calibri', "Do you like to quit Calibri?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        self.show()

    def createTrayIcon(self):
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.maximizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        icon = QIcon("icon.png")
        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

    def createActions(self):
        self.minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        self.maximizeAction = QAction("Ma&ximize", self, triggered=self.showMaximized)
        self.restoreAction = QAction("&Restore", self, triggered=self.showNormal)
        self.quitAction = QAction("&Quit", self, triggered=QApplication.instance().quit)

    def createTrayIcon2(self):
        # Create the icon
        icon = QIcon("icon.png")

        self.clipboard = QApplication.clipboard()
        self.dialog = QColorDialog()

        # Create the menu
        menu = QMenu(self)

        action1 = QAction("Hex")
        #action1.triggered.connect(copy_color_hex)
        menu.addAction(action1)

        action2 = QAction("RGB")
        #action2.triggered.connect(copy_color_rgb)
        menu.addAction(action2)

        menu.addSeparator()

        action3 = QAction("HSV")
        #action3.triggered.connect(copy_color_hsv)
        menu.addAction(action3)

        """
        menu.addAction(self.minimizeAction)
        menu.addAction(self.maximizeAction)
        menu.addAction(self.restoreAction)
        menu.addSeparator()
        menu.addAction(self.quitAction)
        """

        # Create the tray
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(menu)

        self.trayIcon.setIcon(icon)
        self.setWindowIcon(icon)

        # Add the menu to the tray

    def copy_color_hex():
        if dialog.exec_():
            color = dialog.currentColor()
            clipboard.setText(color.name())


    def copy_color_rgb():
        if dialog.exec_():
            color = dialog.currentColor()
            clipboard.setText("rgb(%d, %d, %d)" % (
                color.red(), color.green(), color.blue()
            ))


    def copy_color_hsv():
        if dialog.exec_():
            color = dialog.currentColor()
            clipboard.setText("hsv(%d, %d, %d)" % (
                color.hue(), color.saturation(), color.value()
            ))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calibri()

    sys.exit(app.exec_())
