from tkinter import *
import os, sys

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def get_vars():
    global arguments
    arguments = []
    arguments += [color.get()]
    print(arguments)
    return arguments

def color_handler(color_val):
    if color_val is 'Green':
        return 'color 0a'
    elif color_val is 'Blue':
        return 'color 01'
    elif color_val is 'Red':
        return 'color 04'
    elif color_val is 'White':
        return 'color 07'
    elif color_val is 'Black on White':
        return 'color F0'

global icon
appdata = os.getenv('APPDATA')
if 'win32' in sys.platform: #change this to a settings file to add the python executeable
    icon = r'{}/winguake/icon.ico'.format(appdata)
else:
    icon = r'./data/icon.ico'

root = Tk()

color_text = Label(root, text="Color")
color_text.grid(row=0)
color = StringVar()
color.set('Green')
color_box = OptionMenu(root, color, "Green", "Blue", "Red", "White", "Black on White")
color_box.grid(row=0, column=1)

button = Button(root, text="Getvars", command=get_vars)
button.grid(row=1)

root.mainloop()
