import os, sys
import argparse
import subprocess
import json
#command line handler
parser = argparse.ArgumentParser(description="Guake for Windows")
parser.add_argument('-s', '--settings', help="Open settings", action='store_true')
parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
args = parser.parse_args()
console_running = False
cmd = 'wmic process get description'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if 'console.exe' in str(line):
        console_running = True
    else:
        pass
if args.verbose:
    print("Running WinGuake in Verbose mode.")

if args.settings:
    if args.verbose:
        print("Running settings...")
    os.system('python edit_settings.py')
    #change these around when compiling
    #os.system('guake_settings.exe')
else:
    if not console_running:
        if args.verbose:
            print("WinGuake not started, starting program...")
        os.system('console.exe')
    else:
        if args.verbose:
            print("WinGuake Already running")

    os.system('start_winguake')
