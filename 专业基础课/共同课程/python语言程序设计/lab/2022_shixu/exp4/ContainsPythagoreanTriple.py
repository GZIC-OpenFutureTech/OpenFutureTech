"""
ContainsPythagoreanTriple.py
author:张辰旭
date:2023.04.11
description:takes a list of positive integers and
returns True if there are 3 values (a, b, c) anywhere in the list such that (a,
b, c) form a Pythagorean Triple
"""
def ContainsPythagoreanTriple(d):
    sq = set([x**2 for x in d])
    for i in sq:
        for j in sq:
            if i+j in sq:
                return True
    return False

print(ContainsPythagoreanTriple( [1, 3, 6, 2, 5, 1, 4]))
print(ContainsPythagoreanTriple([1, 3, 6, 2, 1, 4]))


