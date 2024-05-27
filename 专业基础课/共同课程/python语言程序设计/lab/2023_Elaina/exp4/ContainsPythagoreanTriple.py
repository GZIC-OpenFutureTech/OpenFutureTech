"""
ContainsPythagoreanTriple.py
author: Elaina
date: 2023/11/14
description: judge if there are any Pythagorean Triple in the array
"""

def ContainsPythagoreanTriple(L):
    nums_set = set(L)
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if (L[i] ** 2 + L[j] ** 2) in nums_set:
                return True
    return False

numbers = [1, 3, 6, 2, 5, 1, 4]
print(ContainsPythagoreanTriple(numbers))
