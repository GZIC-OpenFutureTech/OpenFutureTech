"""
TagClouds.py
author:张辰旭
date:2023.04.18
description:Statistical buzzword frequency
"""
import re
def split_string(s):
    m = re.match(r'^\D+', s)
    if m:
        prefix = m.group()

        s = s[len(prefix):]
    else:
        prefix = ''
    parts = s.split()
    result = [prefix] + parts
    return result

def TransposeContent(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        n=0
        rows = []
        for line in lines:
            if n != 0:
                rows.append([split_string(line.strip()[1:-1])])
            else:
                rows.append([(line.strip()[1:-1]).split()])
            n=n+1
        cols = [list(row) for row in zip(*rows)]
        with open('transpose_content.txt', 'w') as f_out:
            for j in range(len(cols[0][0])):
                for i in range(len(cols[0])):
                    if i == len(cols[0])-1:
                        f_out.write(cols[0][i][j]+ '\n')
                    else:
                        f_out.write(cols[0][i][j]+',')

while True:
        path = input("Enter the file path: ")
        try:
            with open(path, 'r') as f:
                # If the file can be read, transpose its content and exit the loop
                TransposeContent(path)
                break
        except IOError:
            print("Could not read file, please try again.")