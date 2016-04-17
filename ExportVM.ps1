param(
[string]$server= 0,
[string]$user= 0,
[string]$passwd= 0,
[string]$VM= 0
)

Add-PSSnapin VMware.VimAutomation.Core
Set-PowerCLIConfiguration -InvalidCertificateAction Unset
#$server = Read-Host -Prompt 'Input your server name/IP'
#$user = Read-Host -Prompt 'Input your Login name'
#$passwd= Read-Host -Prompt 'Input your Password'
#$VM= Read-Host -Prompt 'What is the name of the VM you want to export?'
Connect-VIServer $server -User $user -Password $passwd
$test = Get-VM $VM
if ($test.PowerState -eq "PoweredON") {   
 Stop-VM -VM $VM -Kill -Confirm:$false
}
Get-VM -Name $VM* | Export-VApp -Destination "C:\Slyp\"
Import-Module "C:\Program Files\Microsoft Virtual Machine Converter\MvmcCmdlet.psd1"
ConvertTo-MvmcVirtualHardDisk -SourceLiteralPath "C:\Slyp\$VM\'$VM'_disk0.vmdk" -DestinationLIteralPath "C:\Slyp\$VM.vhd"