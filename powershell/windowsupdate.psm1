function updateWindows {
    #Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot
    Get-WUList

}