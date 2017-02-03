import os, sys
import argparse
import subprocess

def chdir(drive, path):
    if 'ENV' in path:
        env_path = os.getenv(path[3:])
    else:
        env_path = path
    if drive is '':
        os.system('c:')
    else:
        os.system(drive)
    os.chdir(env_path)
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
            print("WinGuake Already running!")

    os.system('title WinGuake')
    os.system('python window_resize.py')
    os.system('color 0a')
    startingpath = os.getenv('USERPROFILE')
    os.chdir(startingpath)
    os.system('cls')
    while True:
        current_dir = os.getcwd()
        command = input("{}>".format(current_dir))
        if 'cd' in command[:2]:
            #figure this out later
            os.chdir(command[3:])

        elif command == 'exit':
            sys.exit()
        else:
            os.system(command)
