"""
WordSearch.py
author:Elaina
date:2023/11/13
description:suggests at most three product names from products after each character of searchword is typed.
"""

def match(products, searchWord):
    ans = []
    products.sort()
    for i in range(1, len(searchWord)+1, 1):
        j = 0
        while j < len(products):
            if len(products[j]) < len(searchWord):
                del products[j]
                continue
            if products[j][:i] != searchWord[:i]:
                del products[j]
                continue
            j += 1
        if len(products) <= 3:
            ans.append(products.copy())
        else:
            ans.append(products[0:3].copy())
    print(ans)

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
match(products, searchWord)

products = ["havana"]
searchWord = "havana"
match(products, searchWord)

products = ["bags","baggage","banner","box","cloths"]
searchWord = "bags"
match(products, searchWord)
