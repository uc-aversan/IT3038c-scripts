$RANDO = 0
$Logfile = "C:\logs\rando.log"

for($i = 0; $i -lt 5; $i++) {
    $RANDO=Get-Random -Maximum 1000 -Minimum 1
    Write-Host($RANDO)
    Add-content $Logfile "INFO: Random number is ${RANDO}"
}

#Notes: 
#Hotkeys, F5 = run script
#Shift + F5 = End Debug
#F9 = add breakpoint 