"""
mine_stock_prices.py
author: Elaina
date: 2023/11/21
description: mine the stock prices of Tesla.
"""

import pandas as pd
from operator import itemgetter

def load_daily_data_list(filename):
    file_data = pd.read_csv(filename, sep=',', header=0, encoding='ISO-8859-1')
    columns_to_double = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    file_data[columns_to_double] = file_data[columns_to_double].astype(float)
    list_of_daily_records = []
    for index, row in file_data.iterrows():
        temp = []
        temp.append(row['Date'])
        temp.append(row['Open'])
        temp.append(row['High'])
        temp.append(row['Low'])
        temp.append(row['Close'])
        temp.append(row['Adj Close'])
        temp.append(row['Volume'])
        list_of_daily_records.append(temp)
    return list_of_daily_records

def compute_monthly_average(list_of_daily_records):
    statistic_monthly = '00-0000'
    dividend_sum = 0
    days = 1
    days_all = 0
    monthly_average = []
    for daily_record in list_of_daily_records:
        month = daily_record[0][5:7]
        year = daily_record[0][0:4]
        monthly = month + '-' + year
        if days_all == len(list_of_daily_records) - 1:
            dividend_sum += daily_record[5]
            days += 1
            average = dividend_sum / days
            monthly_list = [average, statistic_monthly]
            monthly_average.append(monthly_list)
            monthly_average.pop(0)
            return tuple(monthly_average)
        elif monthly != statistic_monthly:
            average = dividend_sum / days
            monthly_list = [average, statistic_monthly]
            monthly_average.append(monthly_list)
            statistic_monthly = monthly
            dividend_sum = daily_record[5]
            days = 1
            days_all += 1
        else:
            dividend_sum += daily_record[5]
            days += 1
            days_all += 1
    monthly_average.pop(0)
    return tuple(monthly_average)

def print_extreme_months(list_of_monthly_tuples):
    sorted_list = sorted(list_of_monthly_tuples, key=itemgetter(0), reverse=True)
    for row in sorted_list:
        row[0] = round(row[0], 2)
    print('the six highest monthly averages:')
    for i in range(0, 6, 1):
        print(sorted_list[i])
    sorted_list.reverse()
    print('he six lowest monthly averages:')
    for i in range(0, 6, 1):
        print(sorted_list[i])

path = './SourceFiles/TSLA.csv'
daily_records_list = load_daily_data_list(path)
monthly_average = compute_monthly_average(daily_records_list)
print_extreme_months(monthly_average)
