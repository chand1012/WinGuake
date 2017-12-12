@echo off
rem To use this compiler, autohotkey compiler must be added to path
echo Compiling Winguake...
pyinstaller winguake_allinone.py -n console
echo Compiling launch script...
Ahk2Exe.exe /in compile_changes/Console.ahk /out winguake.exe /icon old/guake_icon.ico
pause
