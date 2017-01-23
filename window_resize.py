import win32api, win32gui
from tkinter import messagebox
import os, sys
import json

def is_default():
    default_settings = {}
    default_settings['color'] = '0a'
    default_settings['directory'] = ''
    default_settings['width'] = ''
    default_settings['height'] = ''
    json_file = open('settings.json')
    parsed_json = json.loads(json_file.read())
    if parsed_json is default_settings:
        return True
    else:
        return False
    json_file.close()

def settings_check():
    exists = os.path.isfile('./settings.json')
    if exists is False:
        messagebox.showinfo('WinGuake', 'Missing settings file, creating default.')
        data = {}
        data['color'] = '0a'
        data['directory'] = ''
        data['width'] = ''
        data['height'] = ''
        json_data = json.dumps(data)
        json_file = open('settings.json', 'w')
        json_file.write(json_data)
        json_file.close()

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'WinGuake' in win32gui.GetWindowText(hwnd):
            settings_check()
            m_width = win32api.GetSystemMetrics(0)
            m_length = win32api.GetSystemMetrics(1)
            json_file = open('settings.json')
            json_data = json.loads(json_file.read)
            if json_data['width'] is '':
                w_width = int(m_width)
            if json_data['height'] is '':
                w_length = int(m_length/2)
            else:
                json_file = open('settings.json')
                settings = json.loads(json_file.read())
                w_width = int(settings['width'])
                w_height = int(settings['height'])
            win32gui.MoveWindow(hwnd, 0, 0, w_width, w_length, True)

def main(home, color): # needs redone
    '''
    if home is '' or home is None:
        home = os.getenv("USERPROFILE")
    os.system('c:')
    os.system("cd {}".format(home))
    '''
    os.system('color {}'.format(color))

win32gui.EnumWindows(enumHandler, None)
main(None, '0a')
