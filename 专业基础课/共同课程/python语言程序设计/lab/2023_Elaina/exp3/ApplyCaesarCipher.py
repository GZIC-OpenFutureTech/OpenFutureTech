"""
ApplyCaesarCipher.py
author:Elaina
date:2023/11/13
description:return a caesar Cipher
"""

def ApplyCaesarCipher(message, shift):
    message2 = []
    for x in message:
        if(x == ' '):
            message2.append(' ')
            continue
        c = chr(ord(x)+shift)
        #print(c)
        if (c > 'z'):
            #print(1)
            message2.append(chr(ord(c) - 26))
        elif(c > 'Z' and c < 'a'):
            #print(2)
            if(x <= 'Z'):
                message2.append(chr(ord(c) - 26))
            else:
                message2.append(chr(ord(c) + 26))
        elif (c < 'A'):
            #print(3)
            message2.append(chr(ord(c) + 26))
        else:
            #print(4)
            message2.append(c)
    return (''.join(message2))

print(ApplyCaesarCipher("We Attack At Dawn", 1))
print(ApplyCaesarCipher("zodiac", -2))
print(ApplyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
print(ApplyCaesarCipher("zodiac", -2) == "xmbgya")

# a = 'a'
# b = chr(ord(a)+2)
# print(b)