import random
import re

char_to_bits = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011',
    'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111',
    'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011',
    'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111',
    'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011',
    'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111',
    'Y': '11000', 'Z': '11001', ' ': '11010', '.': '11011',
    ',': '11100', '?': '11101', '!': '11110', '-': '11111'
}

bits_to_char = {}
for k, v in char_to_bits.items():
    bits_to_char[v] = k


def text_to_bits(text):
    # remove all characters not in char_to_bits and convert to uppercase
    text = re.sub(r'[^A-Z .,?!-]', '', text.upper())
    bits = ""
    for char in text:
        if char in char_to_bits:
            bits += char_to_bits[char]
    return bits


def bits_to_text(bits):
    # split the string of bits into chunks of 5 bits
    pieces = [bits[i:i + 5] for i in range(0, len(bits), 5)]
    text = ""
    # iterate through each piece and convert it to the corresponding character
    for piece in pieces:
        if piece in bits_to_char:
            text += bits_to_char[piece]
    return text


def generate_random_key(length):
    key = ""
    for i in range(length):
        key += random.choice('01')
    return key


def otp_encrypt_decrypt(message_bits, key_bits):
    result = ""
    for m, k in zip(message_bits, key_bits):
        # XOR the bits and add the result to the string
        result += str(int(m) ^ int(k))
    return result


message = "cryptography"
# convert message to bits
message_bits = text_to_bits(message)
# generate random key with the same length as the message bits
key_bits = generate_random_key(len(message_bits))
# encrypt the message
encrypted_bits = otp_encrypt_decrypt(message_bits, key_bits)
# decrypt the message
decrypted_bits = otp_encrypt_decrypt(encrypted_bits, key_bits)

print("Message:", message)
print("Message bits:", message_bits)
print("Key bits:", key_bits)
print("Encrypted data:", encrypted_bits)
print("Decrypted bits:", decrypted_bits)
print("Decrypted message:", bits_to_text(decrypted_bits))
