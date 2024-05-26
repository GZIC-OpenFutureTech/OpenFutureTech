"""
mine_stock_prices.py
author:张辰旭
date:2023.04.18
description:mine_stock_prices
"""
import csv
from collections import defaultdict


def load_daily_data_list(filename):
    daily_records = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip the header row
        for row in reader:
            date = row[0]
            open_price = float(row[1])
            high_price = float(row[2])
            low_price = float(row[3])
            close_price = float(row[4])
            adj_close_price = float(row[5])
            volume = int(row[6])
            daily_records.append([date, open_price, high_price, low_price, close_price, adj_close_price, volume])
    return daily_records


def compute_monthly_averages(list_of_daily_records):
    monthly_records = defaultdict(list)
    for daily_record in list_of_daily_records:
        date = daily_record[0]
        adj_close_price = daily_record[5]
        year_month = '-'.join(date.split('-')[:2])
        monthly_records[year_month].append(adj_close_price)
    monthly_averages = []
    for year_month, prices in monthly_records.items():
        monthly_average = sum(prices) / len(prices)
        monthly_averages.append((monthly_average, year_month))
    return monthly_averages


def print_extreme_months(list_of_monthly_tuples):
    highest_averages = sorted(list_of_monthly_tuples, reverse=True)[:6]
    lowest_averages = sorted(list_of_monthly_tuples)[:6]
    print('{:>15}  {:>15}'.format('High months', 'Low months'))
    print('{:>15}  {:>15}'.format('------------', '-----------'))
    for high_month, low_month in zip(highest_averages, lowest_averages):
        print('{:>15}  {:>15}'.format('{:.2f} ({})'.format(high_month[0], high_month[1]),
                                       '{:.2f} ({})'.format(low_month[0], low_month[1])))


if __name__ == '__main__':
    daily_records = load_daily_data_list('./data/TSLA.csv')
    monthly_averages = compute_monthly_averages(daily_records)
    print_extreme_months(monthly_averages)

