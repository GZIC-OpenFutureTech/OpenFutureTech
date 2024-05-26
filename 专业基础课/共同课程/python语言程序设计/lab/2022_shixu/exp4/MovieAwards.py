"""
MovieAwards.py
author:张辰旭
date:2023.04.11
description:Calculating the number of awards for different films with reduced time complexity
"""
def MovieAwards(oscarResults):
    movieAwards = {}
    for category, movie in oscarResults:
        if movie in movieAwards:
            movieAwards[movie] += 1
        else:
            movieAwards[movie] = 1
    return movieAwards

list_awards = {
("Best Picture", "Green Book"),
("Best Actor", "Bohemian Rhapsody"),
("Best Actress", "The Favourite"),
("Film Editing", "Bohemian Rhapsody"),
("Best Original Score", "Black Panther"),
("Costume Design", "Black Panther"),
("Sound Editing", "Bohemian Rhapsody"),
("Best Director", "Roma")
}

print(MovieAwards(list_awards))