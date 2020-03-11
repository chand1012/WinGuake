import win32gui

def enumHandler(hwnd, lParam):
    name = win32gui.GetWindowText(hwnd)
    if win32gui.IsWindowVisible(hwnd) and name != "":
        print(name)

win32gui.EnumWindows(enumHandler, None)