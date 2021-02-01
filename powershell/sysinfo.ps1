function getIP {
    (Get-NetIPAddress).IPv4Address | select-string "192*"
}

write-host(getIP)
$IP = getIP
write-host("This machine's IP is $IP")



#$Hello = "Hello, powershell!"
#write-Host($Hello)

#Get-Service |select-object * |Out-GridView
#Get-Service | Sort-Object -Property Status -Descending | format-table DisplayName, Status | Out-File C:\temp\services.txt

