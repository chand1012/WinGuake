from json import loads

def getHex(letter):
    thing = open('keyboard.json')
    raw_data = loads(thing.read())
    return raw_data[letter]

def toHex(hex_str):
    return hex(hex_str)

def keyboard(char):
    return toHex(getHex(char))

print(keyboard('a'))
