"""
MovieAwards.py
author: Elaina
date: 2023/11/14
description: get a dictionary mapping each movie to the number of the awards that it won.
"""

def MovieAwards(oscarResults):
    d = dict()
    for elements in oscarResults:
        if elements[1] in d:
            d[elements[1]] += 1
        else:
            d[elements[1]] = 1
    return d

s = {
    ("Best Picture", "Green Book"),
    ("Best Actor", "Bohemian Rhapsody"),
    ("Best Actress", "The Favourite"),
    ("Film Editing", "Bohemian Rhapsody"),
    ("Best Original Score", "Black Panther"),
    ("Costume Design", "Black Panther"),
    ("Sound Editing", "Bohemian Rhapsody"),
    ("Best Director", "Roma")
}

print(MovieAwards(s))