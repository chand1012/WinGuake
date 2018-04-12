import win32gui
from win32api import GetSystemMetrics

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'WinGuake - Guake For Windows' in win32gui.GetWindowText(hwnd):
            m_width = GetSystemMetrics(0)
            m_length = GetSystemMetrics(1)
            w_width = int(m_width)
            w_length = int(m_length/2)
            win32gui.MoveWindow(hwnd, 0, 0, w_width, w_length, True)

def window_resize():
    win32gui.EnumWindows(enumHandler, None)
