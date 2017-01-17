import win32api, win32gui
import os, sys


#old code
'''
def quickresize(columns, lines):c #this may be reused
    os.system("mode con: cols={} lines={}".format(columns, lines))

# try to use the win32 api to grab and move the windows
def move_window(window, x, y, wx, wy):
    win32gui.MoveWindow(window, x, y, wx, wy, True)

def console():
    os.system('start')
    return win32.GetConsoleWindow()
'''

#this is perfect for my PC
#quickresize(192, 25)

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'WinGuake' in win32gui.GetWindowText(hwnd):
            m_width = win32api.GetSystemMetrics(0)
            m_length = win32api.GetSystemMetrics(1)
            w_width = int(m_width)
            w_length = int(m_length/2)
            win32gui.MoveWindow(hwnd, 0, 0, w_width, w_length, True)

win32gui.EnumWindows(enumHandler, None)
