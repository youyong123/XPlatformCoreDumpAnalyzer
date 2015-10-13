import sys
from PyQt4 import QtGui
from coredumputilframe  import Ui_coreDumpUtilFrame
from coredumpHelper  import FileDirHelper

class CoreDumpAttrib:
      __arch = 'MIPS'
      __sysRoot = 'NONE'
      __applicationExe = 'NONE'
      __coreFile = 'NONE'
      

      ''' get the Architecture type - by default, it is MIPS '''  
      def getArchName(self):
          return self. _arch
      '''  sets the Architecture type '''''''''

      def setArchName(self, archName):
          self.__arch = archName

      '''   get the SysRoot Path - it is directory path -- remember  '''
      def getSysRoot(self):
          return self.__sysRoot

      '''  sets the Sysroot Path '''
      def setSysRoot(self, sysRootPath):
           self.__sysRoot = sysRootPath


      '''  get the Application Exe  path and name ------'''
      def getApplicationExe(self):
          return self.__applicationExe

      '''  sets the Application Exe path and name -------'''
      def setApplicationExe(self, AppExe):
          self.__applicationExe = AppExe
    
      '''  get the core file name and path -----'''
      def getCoreFile(self):
          return self.__coreFile

      '''   set the core file name and path -----'''
      def setCoreFile(self, coreFile):   
         self. __coreFile = coreFile

   
def dbgLog(msg):
    # while making the actual product, comment the below line and uncomment pass
    print msg
    #pass 


class Main(QtGui.QMainWindow, Ui_coreDumpUtilFrame):
    def __init__(self):
       QtGui.QMainWindow.__init__(self)
       self.ui= Ui_coreDumpUtilFrame()
       self.ui.setupUi(self)
       self.coreAttrib = CoreDumpAttrib()
       ## added this line to do event driven -- function to be called when the button is clicked 
       self.ui.bSysRootBrowse.clicked.connect(self.ButtonbrowseSysRoot)
       self.ui.bApplicationBrowser.clicked.connect(self.browseApplicationExe)
       self.ui.lCoreFileBrowser.clicked.connect(self.browseCoreFile)
  
 ## browse button event installer ########
  
    def ButtonbrowseSysRoot(self):
        dbgLog('browseSys Root pressed')
        fileHelper = FileDirHelper()
        sysRootDir = fileHelper.getDirPath("SysRootPath")
        self.coreAttrib.setSysRoot(sysRootDir)
        dbgLog (self.coreAttrib.getSysRoot())
        #print getDirPath("GetSysRoot")
  
    def browseApplicationExe(self):
        dbgLog('browse Application Exe')
        fileHelper = FileDirHelper()
        appPathName = fileHelper.getFilePath("Select the Executable")
        self.coreAttrib.setApplicationExe(appPathName)
        dbgLog (self.coreAttrib.getApplicationExe())

    def browseCoreFile(self):
       dbgLog('browse core file')
       fileHelper = FileDirHelper()
       corePathName = fileHelper.getFilePath("Select the CoreFile")
       self.coreAttrib.setCoreFile(corePathName)
       dbgLog (self.coreAttrib.getCoreFile())

     
    
    

 #### browse button event installer completed ###########  

 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
