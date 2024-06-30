from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import randint

keyslist = []

allowedcharacters = []

def CreateKeyAlpha():
    for _ in range(10):    # Lenght of the encryption key
        c = randint(1, 26)
        global sKey
        sKey += ascii_lowercase[c-1]

def CreatekeyNum(random):          # This was unnessesay
    for _ in range(10):    # Lenght of the encryption key
        c = randint(1, random)
        global sKey
        sKey += ascii_lowercase[c-1]



for char in ascii_lowercase:
    sKey = char + ':'
    CreateKeyAlpha()
    allowedcharacters.append(char)

    for keycheck in keyslist:   # Makes shure that key is not repeated for another value
        if sKey == keycheck:
            sKey = char + ':'
            CreateKeyAlpha()

    keyslist.append(sKey)
    
    with open('keys.txt', 'a') as file:
        file.writelines(sKey + '\n')


for char in ascii_uppercase:
    sKey = char + ':'
    CreateKeyAlpha()
    allowedcharacters.append(char)

    for keycheck in keyslist:   # Makes shure that key is not repeated for another value
        if sKey == keycheck:
            sKey = char + ':'
            CreateKeyAlpha()

    keyslist.append(sKey)
    
    with open('keys.txt', 'a') as file:
        file.writelines(sKey + '\n')


for char in digits:
    sKey = char + ':'
    CreatekeyNum(26)
    allowedcharacters.append(char)

    for keycheck in keyslist:   # Makes shure that key is not repeated for another value
        if sKey == keycheck:
            sKey = char + ':'
            CreatekeyNum(26)

    keyslist.append(sKey)
    
    with open('keys.txt', 'a') as file:
        file.writelines(sKey + '\n')


for char in punctuation:
    sKey = char + ':'
    CreatekeyNum(26)
    allowedcharacters.append(char)

    for keycheck in keyslist:   # Makes shure that key is not repeated for another value
        if sKey == keycheck:
            sKey = char + ':'
            CreatekeyNum(26)

    keyslist.append(sKey)
    
    with open('keys.txt', 'a') as file:
        file.writelines(sKey + '\n')




for key in keyslist:
    print(key)

for allow in allowedcharacters:
    with open('allowedlist.txt', 'a') as file:
            file.writelines(allow + '\n')
