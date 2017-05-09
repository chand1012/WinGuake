from tkinter import *
from tkinter import messagebox
import os, sys
import json

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

def ask_reset():
    result = messagebox.askquestion("Reset Settings", "Are You Sure?", icon='warning')
    print(result)
    if 'yes' in result:
        default_settings()

def default_settings():
    #rewrite in JSON
    data = {}
    data['color'] = '0a'
    data['exit'] = 'exit'
    data['minimize'] = 'min'
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
    data['exit'] = settings_list[1]
    data['minimize'] = settings_list[4]
    data['width'] = settings_list[2]
    data['height'] = settings_list[3]
    json_data = json.dumps(data)
    json_file = open('settings.json', 'w')
    json_file.write(json_data)
    json_file.close()
    messagebox.showinfo("WinGuake", "Settings will be applied on next WinGuake restart.")
    sys.exit()

#print(os.path.dirname(os.path.abspath(__file__)))
icon = r'{}/winguake_icon.ico'.format(os.path.dirname(os.path.abspath(__file__)))

root = Tk()

color_text = Label(root, text="Color")
color_text.grid(row=0)
color = StringVar()
color.set('Green')
color_box = OptionMenu(root, color, "Green", "Blue", "Red", "White", "Black on White")
color_box.grid(row=0, column=1)

exit_text = Label(root, text="WinGuake exit command")
exit_text.grid(row=1)
exit_var = StringVar()
exit_box = Entry(root, bd=3, textvariable=exit_var)
exit_box.grid(row=1, column=1)

min_text = Label(root, text="WinGuake minimize command")
min_text.grid(row=1)
min_var = StringVar()
min_box = Entry(root, bd=3, textvariable=min_var)
min_box.grid(row=1, column=1)

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

apply_button = Button(root, text="Apply", command= lambda: apply_settings([color_handler(color.get()), exit_var.get(), width_var.get(), height_var.get(), min_var.get()])).grid(row=5) #1: color, 2: exit, 3: width, 4: height

reset_buttom = Button(root, text="Reset Settings", command=ask_reset).grid(row=5, column=1)
root.title("WinGuake Settings")
try:
    root.iconbitmap(icon)
except:
    print("Icon not found.")

root.mainloop()
