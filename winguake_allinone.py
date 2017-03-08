import os, sys
import argparse
import subprocess
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
    print("Last Dir: ", last_line)
    return last_line.decode('utf-8')

def write_to_log(path, path_to_log):
    pathlog = open('{}\\path.log'.format(path_to_log), 'a')
    pathlog.write('{}\n'.format(path))
    pathlog.close()

def get_setting(thing, default=False):
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
def console_running():
    console_running = None
    cmd = 'wmic process get description'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    if 'console.exe' in str(proc.stdout):
        console_running = True
    else:
        console_running = False
    return console_running

def chdir(path):
    if '%' in path:
        env_var = path.upper().replace('%', '')
        #print(env_var)
        env_path = os.getenv(env_var)
    else:
        env_path = path
    #print(env_path)
    try:
        os.chdir(env_path)
    except:
        print("Path not found!")
#command line handler
parser = argparse.ArgumentParser(description="Guake for Windows")
parser.add_argument('-s', '--settings', help="Open settings", action='store_true')
parser.add_argument('-v', '--verbose', help='Verbose mode', action='store_true')
parser.add_argument('-d', '--defaults', help="Run with default settings", action='store_true')
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
    if not console_running():
        if args.verbose:
            print("WinGuake not started, starting program...")
        os.system('console.exe')
    else:
        if args.verbose:
            print("WinGuake Already running!")

    print("Initializing WinGuake....")
    os.system('title WinGuake - Guake For Windows')
    window_resize()
    os.system(get_setting('color', args.default))
    exit_command = get_setting('exit', args.default)
    minimize_command = get_setting('minimize', args.default)
    startingpath = None
    if not os.path.isdir('logs'):
        os.mkdir('logs')
    if os.path.isfile('{}\\path.log'.format(logpath)):
        pathlog = '{}\\path.log'.format(logpath)
        startingpath = last_line(pathlog)
    else:
        startingpath = os.getenv('USERPROFILE')
    os.chdir(startingpath)
    os.system('cls')
    while True:
        current_dir = os.getcwd()
        write_to_log(current_dir, logpath)
        command = input("{}>".format(current_dir))
        if 'cd' in command[:2]:
            chdir(command[3:])
        elif len(command) is 2 and ':' in command:
            try:
                os.chdir("{}/".format(command))
            except:
                print("Drive not found!")
        elif command == exit_command:
            os.remove("{}\\path.log".format(logpath))
            os.system('exit')
            sys.exit()
        elif command == minimize_command:
            os.system('exit')
            sys.exit()
        elif command == 'ls':
            print(os.listdir())
        else:
            os.system(command)
        print('')
