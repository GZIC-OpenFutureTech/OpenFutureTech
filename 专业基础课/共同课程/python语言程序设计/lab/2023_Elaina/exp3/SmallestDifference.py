"""
SmallestDifference.py
author:Elaina
date:2023/11/13
description:takes a list of integers and returns the smallest absolute difference between any two integers in the list
"""

import math
def SmallestDifference(a:list):
    if(len(a) < 2):
        return -1
    a.sort()
    ans = abs(a[1] - a[0])
    for i in range(0, len(a) - 1, 1):
        ans = min(ans, abs(a[i] - a[i+1]))
    return ans

print(SmallestDifference([19,2,83,6,27]) == 4)