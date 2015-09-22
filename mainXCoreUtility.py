import sys
from PyQt4 import QtGui
from coredumputilframe  import Ui_coreDumpUtilFrame

class Main(QtGui.QMainWindow, Ui_coreDumpUtilFrame):
    def __init__(self):
       QtGui.QMainWindow.__init__(self)
       self.ui= Ui_coreDumpUtilFrame()
       self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
