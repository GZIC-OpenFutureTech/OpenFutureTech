"""
HandlingExceptions.py
author: Elaina
date: 2023/12/12
description: Handle the exceptions in Ex6.0
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

def Encode(key_path):
    print("Please input your plaintext:")
    while True:
        flag = 1
        message = input()
        for c in message:
            if c < 'A' or c > 'Z':
                if c != ' ':
                    flag = 0
                    
        if flag == 1:
            print("Valid input!")
            break
        else:
            print("Invalid input! You must input a valid text! Try again!")
            continue

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
    print(f'Ciper in {ciper_path}')
    return ciper_path

def Decode(key_path, ciper_path):
    with open(key_path, 'rb') as file:
        dic = pickle.load(file)
    with open(ciper_path, 'rb') as file:
        ciper = pickle.load(file)
    
    if type(ciper) != type([]):
        print("Ciper is not a list!")
        raise TypeError("Ciper is not a list!")

    inverse_dic = {}
    for key, val in dic.items():
        inverse_dic[val] = key
    decode_message_list = []
    for _list in ciper:
        if type(_list) == type([]) and len(_list) <= 26:
            decode_message_list.append(inverse_dic[len(_list)])
    decode_message = ''.join(decode_message_list)
    print(f'Your plain text is: {decode_message}')

key_path = Genkey()
ciper_path = Encode(key_path)

# Exception1: TypeError: Ciper is not a list. The following statements will throw a exception.
# with open(ciper_path, 'wb') as file:
#     m = '1'
#     pickle.dump(m, file)

# Exception2: The outer list contains a non-list element.
# li = []
# with open(ciper_path, 'rb') as file:
#     li = pickle.load(file)
#     del li[len(li)-1]
#     li.append('NotList')
# with open(ciper_path, 'wb') as file:
#     pickle.dump(li, file)

# Exception3: There are too many elements in one of the inner lists.
# li = []
# with open(ciper_path, 'rb') as file:
#     error_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#     li = pickle.load(file)
#     li[len(li)-1] = error_list
# with open(ciper_path, 'wb') as file:
#     pickle.dump(li, file)

Decode(key_path, ciper_path)