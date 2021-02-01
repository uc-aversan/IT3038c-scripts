function getIP {
    (Get-NetIPAddress).IPv4Address | select-string "192*"
}

write-host(getIP)
$IP = getIP
$Date = ""
$Body = "This machines IP is $IP. User is $env:username. Hostname is $  . Powershell version $Host.Version.major. Today's date is $."

write-host($Body)





#Send-MailMessage -To "aversan@mail.uc.edu" -From "aversan@mail.uc.edu" -subject "IT3038c windows sysinfo" -body $Body -SmtpServer smpt.google.com -port 587 -usessl -Credential (Get-Credential)


#write-host("This machine's IP is $IP")

#$Hello = "Hello, powershell!"
#write-Host($Hello)

#Get-Service |select-object * |Out-GridView
#Get-Service | Sort-Object -Property Status -Descending | format-table DisplayName, Status | Out-File C:\temp\services.txt

