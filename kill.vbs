' this is to run programs in the background
' rem I am using this as a base for all of the background tasks
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "taskkill /f /im cmd.exe", 0, True

