param(
[string]$server= 0,
[string]$source= 0,
[string]$dest= 0
)
#$server = Read-Host -Prompt 'Input your server name/IP'
#$source= Read-Host -Prompt 'What is the source xml(full path)'
#$dest= Read-Host -Prompt 'What is the destination drivefor the vm'
Import-VM -ComputerName $server -copy -GenerateNewId -Path $source -VhdDestinationPath $dest