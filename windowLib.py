import win32gui
from win32api import GetSystemMetrics
import psutil
import os

WINDOWS = ['WinGuake - Guake For Windows', "Cmder", "MINGW32"]

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        #if 'WinGuake - Guake For Windows' in win32gui.GetWindowText(hwnd) or "Cmder" in win32gui.GetWindowText(hwnd) or "MINGW32" in win32gui.GetWindowText(hwnd): # porting to Cmder
        for window in WINDOWS:
            if window in win32gui.GetWindowText(hwnd):
                m_width = GetSystemMetrics(0)
                m_length = GetSystemMetrics(1)
                w_width = int(m_width)
                w_length = int(m_length/2)
                win32gui.MoveWindow(hwnd, 0, 0, w_width, w_length, True)

def window_resize():
    win32gui.EnumWindows(enumHandler, None)

def is_running(thing):
    return thing in (p.name() for p in psutil.process_iter())

