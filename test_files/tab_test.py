from msvcrt import getch
import os
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

print(tab_function('', None))
count = 0
while True:
    keypress = detect_key()
    if keypress is '\t':
        if count >= tab_function('', None)-1:
            count = 0
        print(tab_function('', count))
        count+=1
    elif keypress is '\r':
        count=0
        print("Count reset!")
    else:
        print(keypress)
