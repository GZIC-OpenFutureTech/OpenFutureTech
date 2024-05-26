"""
SmallestDifference.py
author:张辰旭
date:2023.04.04
description:find the min of sub
"""
def SmallestDifference(a):
    if len(a) < 2:
        return -1
    else:
        min = -1
        a.sort()
        for i in range(1,len(a)-1):
            b = abs(a[i-1]-a[i])
            if (min < 0)or (min > b):
                min = b
        return min

print(SmallestDifference([19,2,83,6,27]) == 4)