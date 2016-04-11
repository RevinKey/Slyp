Add-PSSnapin VMware.VimAutomation.Core
Set-PowerCLIConfiguration -InvalidCertificateAction Unset
Connect-VIServer 192.168.0.5 -User "kierandunbar\reynolds" -Password "g!g@war31"
$test = Get-VM ubuntu
if ($test.PowerState -eq "PoweredON") {   
 Stop-VM -VM ubuntu -Kill -Confirm:$false
}
Get-VM -Name ubuntu* | Export-VApp -Destination "C:\Slyp\"
Import-Module "C:\Program Files\Microsoft Virtual Machine Converter\MvmcCmdlet.psd1"
ConvertTo-MvmcVirtualHardDisk -SourceLiteralPath "C:\Slyp\ubuntu\ubuntu_disk0.vmdk" -DestinationLIteralPath "C:\Slyp\ubuntutest.vhd"