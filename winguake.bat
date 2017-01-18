@echo off
if /I %1=='-settings' python %~dp0/edit_settings.py else cmd /k %~dp0/start_winguake.bat && start "" "Console.ahk"
