import threading
import os, sys
from msvcrt import getch
import keyboard
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')

def detect_key(decode_type='utf-8'):
    key = getch()
    if decode_type == False:
        key = key
    else:
        key = key.decode(decode_type)
    return key

def tab_function(letters='', filenumber=0):
    numletters = len(letters)
    filename = None
    truefiles = []
    filelist = os.listdir()
    for dirfile in filelist:
        if letters in dirfile[:numletters]:
            truefiles += [dirfile]

    if filenumber == None:
        return len(truefiles)
    else:
        return truefiles[filenumber]

def main_tab():
    logging.debug('Starting')
    count = 0
    while True:
        keypress = detect_key()
        logging.debug('Key {} pressed'.format(keypress))
        if keypress is '\t':
            if count >= tab_function('', None)-1:
                count = 0
                selection = tab_function('', count)
                keyboard.write(selection)
                logging.debug('Item {} selected'.format(selection))
                count+=1
            elif keypress is '\r':
                count=0

tabThread = threading.Thread(name='tab_thread', target=main_tab)
tabThread.start()
while True:
    thing = input("Things test:")
    print(thing)
