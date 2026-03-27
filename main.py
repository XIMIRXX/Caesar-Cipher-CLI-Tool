# Make sure art.py is in the same directory

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
            continue

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the result: {cipher_text}")

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid input, please try again!")
        continue
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(text, shift, direction)
    final_answer = input("Do you want to continue? (yes/no): ")
    if final_answer == "no":
        break
