"""
Filemarkets.py
author: Elaina
date: 2023/11/21
description: Get the dictionary of markets and the search for them.
"""

import pandas as pd
def ReadCSV(file_name):
    file_data = pd.read_csv(file_name, sep = '\t', encoding = 'ISO-8859-1')
    file_data.fillna('UNKNOWN', inplace = True)
    file_data.columns = ['state', 'market_name', 'street_address', 'city', 'zip_code', 'longitude', 'latitude']
    return file_data

def GetDictionary(data_frame): 
    zip_code = dict()
    town = dict()
    for index, row_data in data_frame.iterrows():
        row_tuple = (row_data['state'], row_data['market_name'], row_data['street_address'], row_data['city'], row_data['zip_code'], row_data['longitude'], row_data['latitude'])
        # zip code
        if row_data['zip_code'] not in zip_code:
            zip_code[row_data['zip_code']] = (row_tuple,)
        else:
            zip_code[row_data['zip_code']] += (row_tuple,)
        # town
        if row_data['city'] not in town:
            town[row_data['city']] = (row_tuple,)
        else:
            town[row_data['city']] += (row_tuple,)
    return zip_code, town

def Search(zip_code_dict, town_dict):
    while(True):
        print('Please input the zip code or town name that you want to search.')
        request = input()
        flag = True
        if request == 'qu6it':
            return
        if request in zip_code_dict:
            flag = False
            print(zip_code_dict[request])
        if request in town_dict:
            flag = False
            print(town_dict[request])
        if flag:
            print('We find nothing!')

file_name = './SourceFiles/markets.tsv'
markets = ReadCSV(file_name)
zip_code, town = GetDictionary(markets)
Search(zip_code, town)