"""
Filemarkets.py
author:张辰旭
date:2023.04.18
description:Read in documents and sort and search for information
"""
import csv
import pandas as pd
def read_farmers_markets_data(filename):
    zip_to_markets = {}
    town_to_zips = {}
    with open(filename, errors='ignore') as f:
        for line in f:
            fields = line.strip().split('\t')
            state, name, address, city, zipcode, lon, lat = fields
            market = (state, name, address, city, zipcode, lon, lat)
            if zipcode not in zip_to_markets:
                zip_to_markets[zipcode] = []
            zip_to_markets[zipcode].append(market)
            town = city.lower()
            if town not in town_to_zips:
                town_to_zips[town] = set()
            town_to_zips[town].add(zipcode)
    return zip_to_markets, town_to_zips

filename = './data/markets.tsv'
zip_to_markets, town_to_zips = read_farmers_markets_data(filename)
while True:
    query = input("Enter a zip code or a town name (or 'quit' to exit): ").strip().lower()
    if query == 'quit':
        break
    if query.isdigit() and len(query) == 5:
        if query in zip_to_markets:
            print("Farmers markets in zip code", query)
            for market in zip_to_markets[query]:
                print("\t", market[1], "at", market[2], market[3])
        else:
            print("No farmers markets found in zip code", query)
    else:
        if query in town_to_zips:
            print("Farmers markets in", query.title())
            for zipcode in town_to_zips[query]:
                for market in zip_to_markets[zipcode]:
                    if market[3].lower() == query:
                        print("\t", market[1], "at", market[2], zipcode)
        else:
            print("No farmers markets found in", query.title())

