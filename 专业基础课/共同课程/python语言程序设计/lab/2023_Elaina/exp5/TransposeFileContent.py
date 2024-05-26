"""
TransposeFileContent.py
author: Elaina
date: 2023/11/21
description: transpose the file content of each row and corresponding col.
"""

import re

def TransposeFileContent(path):
    matrix = []
    # init
    with open(path, 'r', encoding='ISO-8859-1') as file:
        file_data = file.readlines()
    # to list
    matrix.append(file_data[0].split())
    for line in file_data:
        temp = line.replace('"', '')
        pattern = re.compile(r'(?P<name>[^\d]+)\s+(?P<number>\d+)\s+(?P<numbers>(?:\d+\s*)*)')
        match = pattern.match(temp)
        if match is not None:
            name = match.group('name')
            number = match.group('number')
            numbers = [int(x) for x in match.group('numbers').split()]
            if number[0] == '0':
                name = name + ' ' + number
                number = numbers[0]
                numbers.pop(0)
            temp = []
            temp.append(name)
            temp.append(number)
            temp.extend(numbers)
            matrix.append(temp)
    # transpose
    transposed_matrix = [list(row) for row in zip(*matrix)]
    with open('transpose_content.txt', 'w', encoding='ISO-8859-1') as file:
        for row in transposed_matrix:
            file.write(str(row).replace('[', '').replace(']', '').replace('\'', ''))
            file.write('\n')
    
path = './SourceFiles/author_paper_stat.csv'
TransposeFileContent(path)