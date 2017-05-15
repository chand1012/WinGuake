import os, sys
import argparse
import psutil
import win32api, win32gui
import json

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'WinGuake - Guake For Windows' in win32gui.GetWindowText(hwnd):
            m_width = win32api.GetSystemMetrics(0)
            m_length = win32api.GetSystemMetrics(1)
            w_width = int(m_width)
            w_length = int(m_length/2)
            win32gui.MoveWindow(hwnd, 0, 0, w_width, w_length, True)

def window_resize():
    win32gui.EnumWindows(enumHandler, None)

def last_line(inputfile):
    filesize = os.path.getsize(inputfile)
    blocksize = 1024
    dat_file = open(inputfile, 'rb')
    headers = dat_file.readline().strip()
    if filesize > blocksize :
        maxseekpoint = (filesize // blocksize)
        dat_file.seek(maxseekpoint*blocksize)
    elif filesize :
        maxseekpoint = blocksize % filesize
        dat_file.seek(maxseekpoint)
    lines =  dat_file.readlines()
    if lines :
        last_line = lines[-1].strip()
    print("Last Dir: ", last_line.decode('utf-8'))
    return last_line.decode('utf-8')

def write_to_log(path, path_to_log):
    pathlog = open('{}\\path.log'.format(path_to_log), 'a')
    pathlog.write('{}\n'.format(path))
    pathlog.close()

def get_setting(thing=None, default=False):
    raw_data = None
    if not default:
        try:
            json_file = open('settings.json')
            raw_data = json_file.read()
        except:
            print('JSON file not found!, resorting to defaults')
            raw_data = '{"color": "color 0a", "exit": "exit", "minimize": "min"}'
    else:
        raw_data = '{"color": "color 0a", "exit": "exit", "minimize": "min"}'
    json_data = json.loads(raw_data)
    if thing is '' or thing is None:
        return json_data
    else:
        return json_data[thing]

def is_running(thing):
    return thing in (p.name() for p in psutil.process_iter())

#command line handler
parser = argparse.ArgumentParser(description="Guake for Windows")
parser.add_argument('-s', '--settings', help="Open settings", action='store_true')
parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
parser.add_argument('-d', '--default', help="Run with default settings", action='store_true')
args = parser.parse_args()
logpath = '{}\\logs'.format(os.getcwd())
if args.verbose:
    print("Running WinGuake in Verbose mode.")

if args.settings:
    if args.verbose:
        print("Running settings...")
    os.system('python edit_settings.py')
    #change these around when compiling
    #os.system('guake_settings.exe')
else:
    if not is_running('console.exe'):
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

    print("Initializing WinGuake....")
    os.system('title WinGuake - Guake For Windows')
    window_resize()
    print("Starting with settings: {}".format(get_setting()))
    os.system(get_setting('color', args.default))
    exit_command = get_setting('exit', args.default)
    minimize_command = get_setting('minimize', args.default)
    startingpath = None
    if not os.path.isdir('logs'):
        if not args.verbose:
            print("Logs not found, making new dir...")
        os.mkdir('logs')
    if os.path.isfile('{}\\path.log'.format(logpath)):
        pathlog = '{}\\path.log'.format(logpath)
        startingpath = last_line(pathlog)
    else:
        startingpath = os.getenv('USERPROFILE')
    print("WinGuake Ready!")
    if not args.verbose:
        os.system('cls')

    os.system("cmd /k cd {} && title {}".format(startingpath, "WinGuake - Guake For Windows"))
