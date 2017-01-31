from tkinter import *
from tkinter import messagebox
import os, sys
import json

def get_vars():
    global arguments
    arguments = []
    arguments += [color.get(), dir_var.get(), int(width_var.get()), int(height_var.get())]
    print(arguments)
    return arguments

def color_handler(color_val):
    if color_val is 'Green':
        return '0a'
    elif color_val is 'Blue':
        return '01'
    elif color_val is 'Red':
        return '04'
    elif color_val is 'White':
        return '07'
    elif color_val is 'Black on White':
        return 'F0'

def ask_reset():
    result = messagebox.askquestion("Reset Settings", "Are You Sure?", icon='warning')
    print(result)
    if 'yes' in result:
        default_settings()

def default_settings():
    #rewrite in JSON
    data = {}
    data['color'] = '0a'
    data['directory'] = ''
    data['width'] = ''
    data['height'] = ''
    json_data = json.dumps(data)
    json_file = open('settings.json', 'w')
    json_file.write(json_data)
    json_file.close()
    messagebox.showinfo('WinGuake', 'Settings will be applied on next WinGuake restart.')
    sys.exit()

def apply_settings(settings_list):
    #rewrite in JSON
    data = {}
    data['color'] = settings_list[0]
    data['directory'] = settings_list[1]
    data['width'] = settings_list[2]
    data['height'] = settings_list[3]
    json_data = json.dumps(data)
    json_file = open('settings.json', 'w')
    json_file.write(json_data)
    json_file.close()
    messagebox.showinfo("WinGuake", "Settings will be applied on next WinGuake restart.")
    sys.exit()

#print(os.path.dirname(os.path.abspath(__file__)))
icon = r'{}/guake_icon.ico'.format(os.path.dirname(os.path.abspath(__file__)))

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

apply_button = Button(root, text="Apply", command= lambda: apply_settings([color_handler(color.get()), dir_var.get(), width_var.get(), height_var.get()])).grid(row=5) #1: color, 2: directory, 3: width, 4: height

reset_buttom = Button(root, text="Reset Settings", command=ask_reset).grid(row=5, column=1)
root.title("WinGuake Settings")
try:
    root.iconbitmap(icon)
except:
    print("Icon not found.")

root.mainloop()
