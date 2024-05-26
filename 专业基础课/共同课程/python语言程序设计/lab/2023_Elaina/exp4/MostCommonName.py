"""
MostCommonName.py
author: Elaina
date: 2023/11/14
description: get the most common name from a list of names.
"""

def MostCommonName(L):
    m = dict()
    for names in L:
        if names in m:
            m[names] += 1
        else:
            m[names] = 1
    s = set()
    for key, val in m.items():
        if(val == max(m.values())):
            s.add(key)
    if not s:
        return None
    if len(s) == 1:
        ls = list(s)
        return ls[0]
    return s
    
print(MostCommonName(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron")
print(MostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"})
print(MostCommonName(["Cindy"]) == "Cindy")
print(MostCommonName(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"})
print(MostCommonName([]) == None)
