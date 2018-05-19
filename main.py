"""
main for remote Connexion Organizer.
"""

import sys
import logging
import subprocess

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTreeWidgetItem

import modules.rdpConfig as rdpModule

QTMAINWINDOWSFILE = "Designer/Design_MainWindows.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(QTMAINWINDOWSFILE)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    high level support for doing this and that.
    """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_set.clicked.connect(self.clickSet)
        self.pushButton_Connect.clicked.connect(self.clickConnectBp)
        self.actionExit.triggered.connect(self.close)
        self.pushButtonRDSHelp.clicked.connect(self.RDP_actionHelp)
        self.pushButtonSaveRdp.clicked.connect(self.RDP_actionSave)
        self.pushButtonSetDefaultTreeview.clicked.connect(self.SetDefaultTreeView)

    def clickSet(self):
        RdpConf = rdpModule.RdpConfig("xfreerdp")
        self.lineEditRDSCommand.setText(RdpConf.getDefaultCmd())

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
    
    def SetDefaultTreeView(self):
        l1 = QTreeWidgetItem(["RDP"])
        l2 = QTreeWidgetItem(["SSH"])

        for i in range(3):
            l1_child = QTreeWidgetItem(["Child A" + str(i)])
            l1.addChild(l1_child)

        for j in range(2):
            l2_child = QTreeWidgetItem(["Child AA" + str(j)])
            l2.addChild(l2_child)

        tw = self.treeWidget
        tw.addTopLevelItem(l1)
        tw.addTopLevelItem(l2)
        
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


