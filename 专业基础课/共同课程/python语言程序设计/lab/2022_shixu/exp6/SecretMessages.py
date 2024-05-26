"""
SecretMessages.py
author:张辰旭
date:2023.04.25
description:Translated text
"""
import random
import secrets
import pickle

def generate_random_string():
    random_string = ''.join(secrets.token_urlsafe())
    random_word= ''.join(random.choice(random_string))
    return random_word

def Genkey():
    cipher_numbers = random.sample(range(262), 262)
    cipher_map = {}
    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ "):
        cipher_map[letter] = cipher_numbers[i]
    with open('./data_pickle/cipher_map.pickle', 'wb') as f:
        pickle.dump(cipher_map, f)
    return './data_pickle/cipher_map.pickle'


def Encode(message, cipher_file_path):
    with open(cipher_file_path, "rb") as cipher_file:
        cipher = pickle.load(cipher_file)
        while True:
            message = input()
            a = 0
            encoded_message = []
            for letter in message:
                if letter not in cipher:
                    print(f"Invalid character '{letter}'. Please enter only letters and spaces.")
                    a+=1
                    break
                ciphertext_number = cipher[letter]
                encoded_letter = []
                for i in range(ciphertext_number):
                    encoded_letter.append(generate_random_string())
                encoded_message.append(encoded_letter)
            if a==0:
                with open('./data_result/message_of_answer.pickle', 'wb') as output_file:
                    pickle.dump(encoded_message, output_file)
                return './data_result/message_of_answer.pickle'


def Decode(encoded_file_path, cipher_file_path):
    try:
        with open(encoded_file_path, 'rb') as f:
            encoded_message = pickle.load(f)
            if isinstance(encoded_message, list):
                print("The file contains a list.")
            else:
                print("The file does not contain a list.")
                return
    except (pickle.UnpicklingError, FileNotFoundError):
        print("Failed to load the pickle file.")
        return

    try:
        # Load cipher from file using pickle
        with open(cipher_file_path, "rb") as cipher_file:
            cipher = pickle.load(cipher_file)
    except TypeError:
        print("Invalid cipher format. Please enter a valid cipher.")
        return

    plaintext = ""
    for encoded_letter in encoded_message:
        if not isinstance(encoded_letter, list):
            print(f"Invalid encoded symbol '{encoded_letter}'. Skipping symbol.")
            continue
        if len(encoded_letter) > 216:
            print(f"Too many elements in encoded symbol '{encoded_letter}'. Skipping symbol.")
            continue
        ciphertext_number = len(encoded_letter)
        for letter, number in cipher.items():
            if number == ciphertext_number:
                plaintext += letter
    return plaintext

print("1. Generating encryption schemes")
print("#=========================================================")
filepath = Genkey()
print(f"Saved cipher map to file: {filepath}")
print("Encryption scheme generation complete")
print()
print("2. Enter the information you need to encrypt")
print("#=========================================================")
print("Please enter the characters you need to encrypt:")
message = "JCFBW"
file_answer = Encode(message , filepath)
print(f"save translated message to file: {file_answer}")
print()
print("3. Output of the translated text")
print("#=========================================================")
print(f"the message is: {Decode(file_answer,filepath)}")
