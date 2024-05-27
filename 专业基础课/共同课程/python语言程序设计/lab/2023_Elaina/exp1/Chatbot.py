"""
Chatbot.py
author:Elaina
date:2023/10/23
description:A simple Chatbot
"""
import re
def property(num):
    if(num % 2 == 0):
        return 'even'
    else:
        return 'odd'

def description(gender, age):
    gender_male = ['m', 'boy', 'male']
    gender_female = ['f', 'girl', 'female']
    if(gender in gender_male):
        if(age <= 27):
            return 'young man'
        else:
            return 'man'
    elif(gender in gender_female):
        if(age <= 27):
            return 'young lady'
        else:
            return 'madam'
    else:
        return 'helicopter'

def isqualified_birthday(re_exp, birthday):
    str_format = re.search(re_exp, birthday)
    if(str_format):
        return True
    else:
        return False

def isqualified_gender(gender):
    gender_list = ['male', 'm', 'boy', 'female', 'f', 'girl', 'helicopter']
    if(gender in gender_list):
        return True
    else:
        return False

print('Hello, I am a simple chatbot')
print('What\'s youe name?')
name = str(input())
print('What is your birthday?')
while 1:
    birthday = str(input())
    if(isqualified_birthday('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', birthday)): 
        break
    cnt = 0
    if(isqualified_birthday('((\d{3}[1-9]|\d{2}[1-9]\d|\d[1-9]\d{2}|[1-9]\d{3})(((0[13578]|1[02])(0[1-9]|[12]\d|3[01]))|((0[469]|11)(0[1-9]|[12]\d|30))|(02(0[1-9]|[1]\d|2[0-8]))))|(((\d{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))0229)', birthday)):
        break
    if(isqualified_birthday('((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))', birthday)):
        break
    else:
        print('Please input a valid birthday format (YYYY-MM-DD or YYYYMMDD)!')
year = birthday[0:4]
month = birthday[5:7]
day = birthday[8:10]
print('What is your gender?')
while 1:
    gender = str(input())
    if(isqualified_gender(gender)):
        break
    else:
        print('Please input a valid gender type: \'male\',\'m\',\'boy\',\'female\',\'f\',\'girl\',\'helicopter\'!')
print('What is your favourite number?')
favourite_num = int(input())
age = 2023 - int(year)
print(f'{name} is a 20 years old {description(gender, age)}. His favourite number is {favourite_num}, which is an {property(favourite_num)} number.')
