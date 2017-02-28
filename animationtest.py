import win32api, win32gui

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'WinGuake' in win32gui.GetWindowText(hwnd):
            m_width = win32api.GetSystemMetrics(0)
            m_length = win32api.GetSystemMetrics(1)
            w_width = int(m_width)
            w_length = int(m_length/2)
            for r_height in range(w_width+1): # needs testing, in theory should add one pixel to the terminal really fast, may need timing
                win32gui.MoveWindow(hwnd, 0, 0, w_width, r_height, True)

def window_resize():
    win32gui.EnumWindows(enumHandler, None)