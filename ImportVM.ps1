Add-PSSnapin VMware.VimAutomation.Core
Set-PowerCLIConfiguration -InvalidCertificateAction Unset
Connect-VIServer 192.168.0.5 -User "kierandunbar\reynolds" -Password "g!g@war31"
Import-VApp -Source ".\ubuntu\ubuntu.ovf" -VMHost 192.168.0.4