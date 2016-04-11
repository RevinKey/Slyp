Export-VM -ComputerName rhydon -name Ubuntu-test -path "E:\"  
invoke-command --computername rhydon -scriptblock {Move-Item "E:\Ubuntu-test\Virtual Hard Disks\Ubuntu-test.vhdx" "\\lapras\Slyp\"}
Import-Module "C:\Program Files\Microsoft Virtual Machine Converter\MvmcCmdlet.psd1"
qemu-img convert "Z:\ubuntu-test.vhdx" -O vmdk C:\Slyp\vhdtovmdhUbuntu.vmdk
