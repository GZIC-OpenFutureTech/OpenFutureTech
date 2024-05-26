"""
chatbot.py
author:张辰旭
date:2023.03.21
description:一个对话机器人捏
"""

import datetime
# compute age
def age(birth):
    today = datetime.date.today()
    if birth.month > today.month or (birth.month == today.month and birth.day > today.day):
        age = today.year - birth.year - 1
    else:
        age = today.year - birth.year
    return age

# check the gender
def get_gender(gender):
    if gender.lower() in ['m', 'male', 'boy', 'man']:
        return 'man'
    elif gender.lower() in ['f', 'female', 'girl', 'woman']:
        return 'woman'
    else:
        return 'unkown'

# greeting sentence
print("Hello, I am a simple chatbot")

# input name
name = input("What’s your name？")

# ask birth
while True:
    birthday_str = input("What is your birthday?")
    if len(birthday_str) == 8:
        birthday = datetime.datetime.strptime(birthday_str, '%Y%m%d').date()
        break
    elif len(birthday_str) == 10:
        birthday = datetime.datetime.strptime(birthday_str, '%Y-%m-%d').date()
        break
    else:
        print("please input right form")

# ask gender
while True:
    gender = input("What is your gender? ")
    if gender.lower() in ['m', 'male', 'boy', 'man','f', 'female', 'girl', 'woman']:
        break
    else:
        print("please input right form")

# ask favorite numble
favorite_number = int(input("What is your favorite number?"))

# compute the age
age = age(birthday)

# even or odd
if favorite_number % 2 == 0:
    even_odd = 'even'
else:
    even_odd = 'odd'

# give a sentence
gender_description = get_gender(gender)
print(f"{name} is a {age}years old {gender_description}，His favorite number is {favorite_number}，which is an {even_odd}number")
