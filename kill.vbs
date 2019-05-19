' this is to run programs in the background
' rem I am using this as a base for all of the background tasks
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "taskkill /f /im cmd.exe", 0, True
WshShell.Run "taskkill /f /im ConEmu64.exe", 0, True ' this will also kill cmder instances
