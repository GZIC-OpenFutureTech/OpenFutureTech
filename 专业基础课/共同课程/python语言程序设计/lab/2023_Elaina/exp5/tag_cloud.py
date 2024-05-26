"""
TagClouds.py
author: Elaina
date: 2023/11/21
description: Generate a word frequency of some texts.
"""

import re

names = {
    'OBAMA', 'ROMNEY', 'LEHRER'
}

def GetStopWords():
    stopwords = set()
    with open('data.txt', 'r') as file:
        for line in file:
            word = line.strip()
            stopwords.add(word)
    return stopwords
    
def GetText(file_name):
    with open(file_name) as file:
        file_data = file.read()
        file_data = re.sub(r'\([^)]*\)', ' ', file_data)
        for symbol in '''!"$%&()*+,-./;:<=>?@[\\]^_{|}~''\n\t ''':
            file_data = file_data.replace(symbol, ' ')
    return file_data

def GetFrequency(file_data, spoken_name):

    stopwords = GetStopWords()

    words = file_data.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    words_of_name = []
    frequency = dict()
    i = 0
    pos = 0
    flag = 0
    while i < len(words):
        if words[i].upper() == spoken_name:
            pos = i
            flag = 1
        elif words[i].upper() in names and flag == 1: 
            words_of_name.extend(words[pos:i])
            flag = 0
        i += 1

    words_of_name = [word for word in words_of_name if not word.isdigit()]
    stopwords_set = set()
    
    for word in words_of_name:
        if word in stopwords:
            stopwords_set.add(word)
        else:
            frequency[word]=frequency.get(word, 0)+1

    with open('./stop-words.txt', 'w') as file:
         for word in stopwords_set:
            file.write(word)
            file.write('\n')

    del frequency[spoken_name.lower()]
    return frequency

def main(file_name, spoken_name):
    result_file_name = spoken_name + '.txt'
    spoken_name = spoken_name.upper()
    if spoken_name not in names:
        raise Exception("Invalid speaker name!")
    text = GetText(file_name)
    frequency = GetFrequency(text, spoken_name)
    sorted_frequency = sorted(frequency.items(), key=lambda x : x[1], reverse=True)
    times = 0
    with open(result_file_name, 'w') as file:
        for word, freq in sorted_frequency:
            if times == 40:
                break
            file.write(f"{word}: {freq}\n")
            times += 1

#main('./SourceFiles/2012-debate-01-partial.txt', 'OBAMA')
main('./SourceFiles/2012-debate-01.txt', 'Romney')