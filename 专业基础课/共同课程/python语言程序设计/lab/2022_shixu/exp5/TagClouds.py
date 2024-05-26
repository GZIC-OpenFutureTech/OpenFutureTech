"""
TagClouds.py
author:张辰旭
date:2023.04.18
description:Statistical buzzword frequency
"""
import matplotlib.pyplot as plt
from os import path
from imageio import imread
from wordcloud import WordCloud
import re
import string

def main(filepath, spoken_name):
    word_count = []
    with open('./data/stop-words.txt', 'r') as stop_file:
        stop_words = set([line.strip() for line in stop_file])
    with open(filepath, 'r') as file:
        text = file.read()
    punctuations = string.punctuation
    pattern = spoken_name.upper() + r':\s+'
    speaker_text = re.split(pattern, text)[1:]
    speaker_words = ' '.join(speaker_text).split()
    speaker_dict = {}
    for word in speaker_words:
        if word == '':
            break
        word = word.translate(str.maketrans('', '', punctuations))
        if word.lower() not in stop_words:
            word_count.append(word)
            if word in speaker_dict:
                speaker_dict[word] += 1
            else:
                speaker_dict[word] = 1
    top_words = sorted(speaker_dict.items(), key=lambda x: x[1], reverse=True)[:40]
    with open(spoken_name + '.txt', 'w') as output_file:
        for word, count in top_words:
            output_file.write(f'{word}: {count}\n')
    return word_count
name = 'LEHRER'
word_count = main('./data/2012-debate-01.txt', 'LEHRER')
d = path.dirname(__file__)
mask_image = imread(path.join(d, "./fig/fig.png"))
content = ' '.join(word_count)
wordcloud = WordCloud(font_path='simhei.ttf', background_color="white", mask=mask_image, max_words=40).generate(content)
# Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
wordcloud.to_file('./fig/wordcloud'+name +'.jpg')
plt.show()
