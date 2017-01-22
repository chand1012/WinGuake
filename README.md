# WinGuake
A Windows-oriented version of the popular Guake Terminal for Linux. Check out the original Linux version here: https://github.com/Guake/guake/
# Prerequisites
Eventually I will make a pre-compiled version for those who want to not need these requirements, but is currently not complete. Currently, you need a working version of [Python](http://python.org) 3.x with Tkinter (Python 2.x is untested) installed and added to PATH, have [AutoHotKey](https://autohotkey.com/) installed, and the latest version of [PyWin32](https://sourceforge.net/projects/pywin32/).
# How to use
After the requirements are met, clone the repository to a safe location (or download as a ZIP):
`git clone https://github.com/chand1012/winguake.git`
Double click Console.ahk or run guake.bat and just press Ctrl+Alt+T. Something like this should show up:
![](https://i.imgur.com/LbEgJKY.png)
To exit, just type `exit` into the console. AutoHotKey will run in the background for when you need to bring up the CMD again.
# Planned Features
- Get settings working correctly
- Finish Settings editor
- Custom starting directories and color changing
- Pre-compiled installer
