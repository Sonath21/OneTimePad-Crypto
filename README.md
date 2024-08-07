# One-Time Pad Cryptography

This Python project implements a simple cryptographic system using the One-Time Pad (OTP) method. The OTP is a symmetric encryption technique where a random key is used only once to encrypt a message. The key must be as long as the message, making it theoretically unbreakable if used correctly.

## Features
- **Character to Bits Conversion**: Maps characters to their corresponding 5-bit binary representation.
- **Bits to Character Conversion**: Maps 5-bit binary strings back to their corresponding characters.
- **Text to Bits**: Converts a given text message to a string of bits.
- **Bits to Text**: Converts a string of bits back to the original text message.
- **Random Key Generation**: Generates a random binary key of specified length.
- **OTP Encryption/Decryption**: Encrypts and decrypts messages using the OTP method.

## Functions

### `text_to_bits(text)`
Converts a given text message to a string of bits, removing any characters not in the predefined character set and converting to uppercase.
- **Parameters**: `text` (str) - The text message to be converted.
- **Returns**: (str) - The resulting string of bits.

### `bits_to_text(bits)`
Converts a string of bits back to the original text message by mapping each 5-bit chunk to its corresponding character.
- **Parameters**: `bits` (str) - The string of bits to be converted.
- **Returns**: (str) - The resulting text message.

### `generate_random_key(length)`
Generates a random binary key of the specified length.
- **Parameters**: `length` (int) - The length of the key to be generated.
- **Returns**: (str) - The resulting random key.

### `otp_encrypt_decrypt(message_bits, key_bits)`
Encrypts or decrypts a message using the OTP method by XORing each bit of the message with the corresponding bit of the key.
- **Parameters**: 
  - `message_bits` (str) - The bits of the message to be encrypted or decrypted.
  - `key_bits` (str) - The bits of the key.
- **Returns**: (str) - The resulting encrypted or decrypted bits.

