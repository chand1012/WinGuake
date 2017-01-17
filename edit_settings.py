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
    arguments += [color.get(), dir_var.get(), int(width_var.get()), int(height_var.get())]
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
icon = r'{}/winguake/icon.ico'.format(appdata)

root = Tk()

color_text = Label(root, text="Color")
color_text.grid(row=0)
color = StringVar()
color.set('Green')
color_box = OptionMenu(root, color, "Green", "Blue", "Red", "White", "Black on White")
color_box.grid(row=0, column=1)

dir_text = Label(root, text="WinGuake starting directory")
dir_text.grid(row=1)
dir_var = StringVar()
dir_box = Entry(root, bd=3, textvariable=dir_var)
dir_box.grid(row=1, column=1)

width_text = Label(root, text="WinGuake starting width")
width_text.grid(row=2)
width_var = StringVar()
width_box = Entry(root, bd=3, textvariable=width_var)
width_box.grid(row=2, column=1)

height_text = Label(root, text="WinGuake starting height")
height_text.grid(row=3)
height_var = StringVar()
height_box = Entry(root, bd=3, textvariable=height_var)
height_box.grid(row=3, column=1)


button = Button(root, text="Apply", command=get_vars)
button.grid(row=5)

root.title("WinGuake Settings")
try:
    root.iconbitmap(icon)
except:
    print("Icon not found.")

root.mainloop()
