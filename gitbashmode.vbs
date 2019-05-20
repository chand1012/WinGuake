Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "git-bash", 0, True
WScript.Sleep 1000
WshShell.Run "python winguake2.py -m bash", 0, True ' this will need changed for the production exe