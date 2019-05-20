Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "taskkill /f /im bash.exe", 0, True