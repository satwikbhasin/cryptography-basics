# Text Encryption and Decryption Tool

This Python tool implements a combination of three cryptographic techniques — Substitution, Transposition, and Product Encryption — to encrypt and decrypt messages. It was developed as part of the ICSI 526 Cryptography class at SUNY Albany. The tool demonstrates basic cryptography concepts and allows for encryption and decryption of text using a user-defined key.

## Features

- **Substitution Cipher**: Shifts letters by a fixed number in the alphabet (both for encryption and decryption).
- **Transposition Cipher**: Reverses the string to add an additional layer of encryption.
- **Product Encryption**: Uses modular arithmetic to further encrypt the text based on the key.

## How It Works

1. **Substitution Encryption**: Each letter is shifted by a key value in the alphabet (e.g., a key of 3 shifts 'a' to 'd').
2. **Transposition Encryption**: The string is reversed, adding another level of transformation.
3. **Product Encryption**: The letters are converted into numbers (0-25), multiplied by a key, and taken modulo 26 to get the encrypted letter.

The decryption process reverses these transformations in the opposite order, recovering the original message.

## Prerequisites

- Python 3.x installed on your machine.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate into the project directory:
   ```bash
   cd your-repo-name
   ```

## Usage

1. Open a terminal and navigate to the folder containing the `q3.py` file.
2. Run the script:
   ```bash
   python q3.py
   ```

3. Enter the **plaintext** and **key** when prompted.

4. The script will output:
   - The **encrypted text**.
   - The **decrypted text**, which should match the original plaintext.

## Example

### Sample Run:
```bash
Enter the plaintext: Hello, World!
Enter the key in integer [Do not use keys that have common factors with '26' other than '1'!]: 5
Encrypted text: mjjvs, bjvsr!
Decrypted text: Hello, World!
```

### Key Validation:
The key entered must be coprime with 26 (i.e., it should not share any common divisors with 26, other than 1). If an invalid key is entered, the program will prompt for a valid one.

## Code Overview

- `substitution(text, substitution_key, inverse=False)`: Encrypts or decrypts the text using a Caesar cipher-like substitution based on the key.
- `transposition(text)`: Reverses the string for additional encryption or decryption.
- `productEncryption(text, key)`: Encrypts the text using modular arithmetic (product cipher).
- `productDecryption(cipher, key)`: Decrypts the cipher using the modular inverse of the key.
- `encrypt(text, key)`: Combines substitution, transposition, and product encryption for the final encrypted text.
- `decrypt(cipher, key)`: Reverses the combined encryption process to return the original text.

---
