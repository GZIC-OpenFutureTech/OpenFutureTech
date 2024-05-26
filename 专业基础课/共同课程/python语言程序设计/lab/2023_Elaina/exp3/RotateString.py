"""
RotateString.py
author:Elaina
date:2023/11/13
description:return the string s rotated k or |k| palces to the left/right.
"""

def RotateString(s:str, k:int):
    if k == 0:
        return s
    elif k > 0:
        s1 = s[:k]
        s2 = s[k:]
        return s2 + s1
    elif k < 0:
        k = -k
        s1 = s[:len(s)-k]
        s2 = s[len(s)-k:]
        return s2 + s1
    
print(RotateString('abcd', 1))
print(RotateString('abcd', -1))    
print(RotateString('abcd', 1) == 'bcda')
print(RotateString('abcd', -1) == 'dabc')