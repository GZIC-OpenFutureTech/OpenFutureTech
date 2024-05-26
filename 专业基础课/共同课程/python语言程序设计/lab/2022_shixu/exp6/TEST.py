import random
import secrets
import pickle

def generate_random_string():
    random_string = ''.join(secrets.token_urlsafe())
    random_word= ''.join(random.choice(random_string))
    return random_word

def Genkey():
    cipher_numbers = random.sample(range(1000), 1000)
    cipher_map = {}
    for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ "):
        cipher_map[letter] = cipher_numbers[i]
    with open('./data_pickle/cipher_map_test.pickle', 'wb') as f:
        pickle.dump(cipher_map, f)
    return './data_pickle/cipher_map_test.pickle'


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
                with open('./data_result/message_of_answer_test.pickle', 'wb') as output_file:
                    pickle.dump(encoded_message, output_file)
                return './data_result/message_of_answer_test.pickle'
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