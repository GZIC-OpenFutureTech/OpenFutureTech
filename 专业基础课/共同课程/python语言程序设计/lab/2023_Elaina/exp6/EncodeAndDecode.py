"""
EncodeAndDecode.py
author: Elaina
date: 2023/12/12
description: Generate the key and save the plaintext, then decode the message
"""

import pickle, random, os

def Genkey():
    dic = dict()
    number_list = [i for i in range(0, 27, 1)]
    char_list = [' ']
    c = 'A'
    while c <= 'Z':
        char_list.append(c)
        c = chr(ord(c)+1)
        
    while len(number_list) != 0:
        len_num = len(number_list)
        len_chr = len(char_list)
        r1 = random.randint(0, len_num-1)
        r2 = random.randint(0, len_chr-1)
        dic[char_list[r2]] = number_list[r1]
        del number_list[r1]
        del char_list[r2]

    with open('Genkey.pkl', 'wb') as file:
        pickle.dump(dic, file)

    file_path = os.path.abspath('Genkey.pkl')

    return file_path

def Encode(message, key_path):
    with open(key_path, 'rb') as file:
        dic = pickle.load(file)
    message_per_char = list(message)
    ciper = []
    for c in message_per_char:
        num = dic[c]
        temp = [1 for i in range(num)]
        ciper.append(temp)
    
    with open('Ciper.pkl', 'wb') as file:
        pickle.dump(ciper, file)

    ciper_path = os.path.abspath('Ciper.pkl')
    print(ciper_path)
    return ciper_path

def Decode(key_path, ciper_path):
    with open(key_path, 'rb') as file:
        dic = pickle.load(file)
    with open(ciper_path, 'rb') as file:
        ciper = pickle.load(file)
    inverse_dic = {}
    for key, val in dic.items():
        inverse_dic[val] = key
    decode_message_list = []
    for _list in ciper:
        decode_message_list.append(inverse_dic[len(_list)])
    decode_message = ''.join(decode_message_list)
    print(decode_message)

key_path = Genkey()
ciper_path = Encode('MARY', key_path)
Decode(key_path, ciper_path)