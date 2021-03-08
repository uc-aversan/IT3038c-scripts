# MY Github repo for IT3038C

### Lab 7
Welcome!
This is how to run a Powershell Script that I created, which uses a plugin called PSWindowsUpdate.
First, We'll create a Virtual ENV called scripts. You can call it whatever you want. 

```powershell
C:\IT3038c-scripts\powershell> C:\venv\webscraping\Scripts\activate.ps1
```

We can then ensure that the module is installed and imported.

```powershell
C:\IT3038c-scripts\powershell> Install-Module -Name PSWindowsUpdate
C:\IT3038c-scripts\powershell> Import-Module PSWindowsUpdate
```

To run the script I made:

```powershell
C:\IT3038c-scripts\powershell> updateWindows
```

This will output a list of updates available to the device.
Other capabilities of this module include the folowing:

```powershell
C:\IT3038c-scripts\powershell> Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot

C:\IT3038c-scripts\powershell> Remove-WindowsUpdate -KBArticleID KB0000000 -NoRestart
```

This first, will automatically download and install all updates available to the device.
The Second if the KBArticleID arguement is replaced with an actual KB number, will uninstall the listed update, pending system restart.

I hope this has effectively showcased the PSWindowsUpdate module, including the potential dangers of such modules like this one's ability to selectively uninstall updates.
finally we deactivate the virtualenv when finished

```powershell
deactivate
```