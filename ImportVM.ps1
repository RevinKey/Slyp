param(
[string]$server= 0,
[string]$user= 0,
[string]$passwd= 0,
[string]$source= 0
)
Add-PSSnapin VMware.VimAutomation.Core
Set-PowerCLIConfiguration -InvalidCertificateAction Unset
#$server = Read-Host -Prompt 'Input your server name/IP'
#$user = Read-Host -Prompt 'Input your Login name'
#$passwd= Read-Host -Prompt 'Input your Password'
#$source= Read-Host -Prompt 'What is the source ovf(full path)'
Connect-VIServer 192.168.0.5 -User $user -Password $passwd
Import-VApp -Source $source -VMHost $server