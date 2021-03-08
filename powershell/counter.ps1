$Machines = 'aversan-win'
$logfile = "C:\logs\counterdata.log"
$date = Get-Date

Foreach ($machine in $Machines) {
    #$RCounters = get-counter -Listset * -ComputerName $machine 
    #"There are {0} counters on {1}" -f $RCounters.count, ($machine)

    $pt = (get-counter -counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 5).CounterSamples.CookedValue
    $sample = 1
    foreach ($p in $pt) {
        "{3} Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample, $date | Out-File -Append $logfile 
        $sample++
    }
}