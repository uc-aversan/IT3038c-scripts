function getIP {
    (Get-NetIPAddress).IPv4Address | select-string "192*"
    #return $IP.IPv4Address 
}