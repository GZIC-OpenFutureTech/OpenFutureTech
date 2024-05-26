"""
ApplyCaesarCipher.py
author:张辰旭
date:2023.04.04
description:Encryption by shifting alphabetical order
"""
def ApplyCaesarCipher(message, shift):
    result = ""
    for c in message:
        if c.isupper():
            result += chr((ord(c) - 65 + shift) % 26 + 65)
        elif c.islower():
            result += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            result += c
    return result

print(ApplyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
print(ApplyCaesarCipher("zodiac", -2) == "xmbgya")
