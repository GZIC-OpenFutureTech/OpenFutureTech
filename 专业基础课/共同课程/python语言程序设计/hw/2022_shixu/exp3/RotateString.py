"""
RotateString.py
author:张辰旭
date:2023.04.04
description:Implementing different order of string output
"""
def RotateString(s, k):
    n = len(s)
    if k < 0:
        k = n + k
    k = k % n
    return s[k:] + s[:k]

print(RotateString ('abcd',  1) == 'bcda')
print(RotateString ('abcd', -1) == 'dabc')
