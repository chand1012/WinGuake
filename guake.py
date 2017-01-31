import os, sys
import argparse

#command line handler
parser = argparse.ArgumentParser(description="Guake for Windows")
parser.add_argument('-s', '--settings', help="Open settings", action='store_true')
args = parser.parse_args()

if args.settings:
    os.system('python edit_settings.py')
    #change these around when compiling
    #os.system('guake_settings.exe')
else:
    os.system('cmd /k start_winguake')
