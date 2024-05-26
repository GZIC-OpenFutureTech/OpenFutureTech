"""
WordSearch.py
author:张辰旭
date:2023.04.04
description:Give search suggestions based on prefixes
"""
def WordSearch(products,searchWord):
    result = []
    products.sort()
    prefix = ""
    for Alphabet in searchWord:
        prefix += Alphabet
        Num = []
        for product in products:
            if product.startswith(prefix):
                Num.append(product)
            if len(Num) == 3:
                break
        result.append(Num)
    return result

print(WordSearch(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))
print(WordSearch(products = ["havana"], searchWord = "havana"))
print(WordSearch(products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"))
