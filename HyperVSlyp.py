import subprocess
import sys
from ConfigParser import SafeConfigParser



class hyperV():

    parser = SafeConfigParser()
    parser.read('config.ini')
    exportpath=parser.get('HyperV','exportpath')
    vmname=parser.get('HyperV','vmnameHV')
    VHDpath=parser.get('HyperV','vhd_path')
    hyperv=parser.get('HyperV','hyperv')
    xml_path = ('HyperV','xml_path')
    statusout = ('HyperV','stdout_path')
    def importVHD(self):
        #p=subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","-NoProfile", "-ComputerName","rhydon", "-copy", "-GenerateNewId", "-Path", "e:\\export\\dumbgarbageignoreme\\WindowsVM\\Virtual Machines\\AD27FDF1-1762-46F2-ADCB-525468D060E7.XML'", "-VhdDestinationPath", "e:\defaultvmrepo\trash2"])
	p=subprocess.call(["powershell.exe","C:\\Slyp\\hypervimport.ps1",self.hyperv, self.xml_path, self.VHDpath])
    def exportVHD(self):
        p=subprocess.call(["powershell.exe","C:\\Slyp\\hypervexport.ps1",self.hyperv, self.vmname, self.exportpath])
        
    def PowerON(self):
        p=subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","-NoProfile", "Start-VM", "-ComputerName", self.hyperv, "-Name", self.vmname])
        
    def PowerOff(self):
        p=subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","-NoProfile", "Stop-VM", "-ComputerName", self.hyperv, "-Name", self.vmname])
       
    def getVMs(self):
        p=subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","-NoProfile", "Get-VM", "-ComputerName", self.hyperv])
       
