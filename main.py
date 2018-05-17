import sys, logging, os
import subprocess

from PyQt5 import QtWidgets, uic
 
qtMainwindowsFile = "Designer/Design_MainWindows.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtMainwindowsFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_set.clicked.connect(self.clickSet)
        self.pushButton_Connect.clicked.connect(self.clickConnectBp)
        self.actionExit.triggered.connect(self.close)
        self.pushButtonRDSHelp.clicked.connect(self.RDP_actionHelp)
        self.pushButtonSaveRdp.clicked.connect(self.RDP_actionSave)

    def clickSet(self):
        self.lineEditRDSCommand.setText('xfreerdp --plugin cliprdr --ntlm --composition -x m -u Administrator -p "xxxxxxxx" -g 1920x1000 xxxxxxx')

    def clickConnectBp(self):
        logging.debug('A debug message!')
        logging.info('Execute command: %s', self.lineEditRDSCommand.text())
        subprocess.Popen(self.lineEditRDSCommand.text(), shell=True)  # returns the exit code in unix

    def RDP_actionHelp(self):
        RDPHelpMessageBox = QtWidgets.QMessageBox(self)
        logging.debug('Execute RDP Help Command')
        RDPHelpMessageBox.setText(subprocess.run(['xfreerdp', '--help'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
        RDPHelpMessageBox.setWindowTitle('RDP Help')
        RDPHelpMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        return RDPHelpMessageBox.exec_()

    def RDP_actionSave(self):
        # do nothing
        pass


def InitApp():
    # Open or create json save file
    saveFile = open("default.json", 'w')
    return saveFile
    
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    saveFile = InitApp()
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


