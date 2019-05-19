import win32gui

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        print(win32gui.GetWindowText(hwnd))

win32gui.EnumWindows(enumHandler, None)