param(
[string]$server= 0,
[string]$VM= 0,
[string]$path= 0
)

#$server = Read-Host -Prompt 'Input your server name/IP'
#$VM= Read-Host -Prompt 'What is the VM name'
#$path= Read-Host -Prompt 'What is the export path(full path)'
Export-VM -ComputerName $server -name $VM -path $path  
invoke-command --computername $server -scriptblock {Move-Item "$path\Virtual Hard Disks\$VM.vhdx" "C:\Slyp\"}
Import-Module "C:\Program Files\Microsoft Virtual Machine Converter\MvmcCmdlet.psd1"
qemu-img convert "C:\Slyp\$VM.vhdx" -O vmdk C:\Slyp\vhdtovmdk.vmdk
