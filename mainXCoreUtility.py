import sys
from PyQt4 import QtGui
from coredumputilframe  import Ui_coreDumpUtilFrame

def dbgLog(msg):
    # while making the actual product, comment the below line and uncomment pass
    print msg
    #pass 


class Main(QtGui.QMainWindow, Ui_coreDumpUtilFrame):
    def __init__(self):
       QtGui.QMainWindow.__init__(self)
       self.ui= Ui_coreDumpUtilFrame()
       self.ui.setupUi(self)
       ## added this line to do event driven -- function to be called when the button is clicked 
       self.ui.bSysRootBrowse.clicked.connect(self.ButtonbrowseSysRoot)
       self.ui.bApplicationBrowser.clicked.connect(self.browseApplicationExe)
       self.ui.lCoreFileBrowser.clicked.connect(self.browseCoreFile)
  
 ## browse button event installer ########
  
    def ButtonbrowseSysRoot(self):
        dbgLog('browseSys Root pressed')
  
    def browseApplicationExe(self):
        dbgLog('browse Application Exe')

    def browseCoreFile(self):
       dbgLog('browse core file')

 #### browse button event installer completed ###########  

 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
