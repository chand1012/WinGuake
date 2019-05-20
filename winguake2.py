from windowLib import *
import sys, os
import argparse

temp_dir = os.path.dirname(os.path.realpath(__file__))
#dir = "."

parser = argparse.ArgumentParser(description="Guake for Windows")
#parser.add_argument('-s', '--settings', help="Open settings", action='store_true')
parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
parser.add_argument('-m', '--mode', help="Sets what mode to use", action='store', type=str)
#parser.add_argument('-d', '--default', help="Run with default settings", action='store_true')
args = parser.parse_args()

if args.mode=='' or 'winguake' in args.mode.lower():
    WINDOWTEST = WINDOWS[0]
elif 'bash' in args.mode.lower():
    WINDOWTEST = WINDOWS[2]
elif 'cmder' in args.mode.lower():
    WINDOWTEST = WINDOWS[1]
    
if args.verbose:
    print("Running WinGuake in Verbose mode.")
'''
if False:
    if args.verbose:
        print("Running settings...")
    os.system('python edit_settings.py')
    #change these around when compiling
    #os.system('winguake_settings.exe')
'''
#else:
if not is_running('console.exe') and not is_running('AutoHotkey.exe'):
    if args.verbose:
        print("WinGuake not started, starting program...")
    run_console = os.system('console.exe')
    if int(run_console) != 0:
        if args.verbose:
            print("WinGuake precompiled script not found, seeing if AutoHotkey is running...")
        if not is_running('AutoHotkey.exe'):
            if args.verbose:
                print('AutoHotkey is not running, trying to run...')
            run_console_b  = os.system('start Console.ahk')
            if int(run_console_b) != 0:
                if args.verbose:
                    print("No console script found, skipping....")
        else:
            if args.verbose:
                print('AutoHotkey is already running!')
else:
    if args.verbose:
        print("WinGuake Already running!")

if not args.verbose:
    os.system("cls")
#dir = get_dir() get this working
folder = os.getenv("USERPROFILE")

os.chdir(folder)
window_resize()
