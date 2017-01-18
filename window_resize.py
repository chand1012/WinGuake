import win32api, win32gui
import os, sys
from configparser import *


def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'WinGuake' in win32gui.GetWindowText(hwnd):
            m_width = win32api.GetSystemMetrics(0)
            m_length = win32api.GetSystemMetrics(1)
            w_width = int(m_width)
            w_length = int(m_length/2)
            win32gui.MoveWindow(hwnd, 0, 0, w_width, w_length, True)

def main(home, color):
    '''
    if home is '' or home is None:
        home = os.getenv("USERPROFILE")
    os.system('c:')
    os.system("cd {}".format(home))
    '''
    os.system('color {}'.format(color))

win32gui.EnumWindows(enumHandler, None)
main(None, '0a')
