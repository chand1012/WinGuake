Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "taskkill /f /im ConEmu64.exe", 0, True ' this will also kill cmder instances
WshShell.Run "taskkill /f /im ConEmuC64.exe", 0, True
WScript.Sleep 100
WshShell.Run "taskkill /f /im cmd.exe", 0, True