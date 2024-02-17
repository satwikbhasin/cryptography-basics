

# Instructions
# 1. Make sure you have python installed on your computer
# 2. Open terminal and go to the folder that has my source code file (q3.py)
# 3. In the terminal, type "python q3.py"
# 4. Follow the prompts


# -------------------------Substitution--------------------------

def substitution(text, substitution_key, inverse=False):
    substituted_text = ""
    # Calculate the inverse key if inverse=True
    inverse_key = -substitution_key if inverse else substitution_key
    for char in text:
        if char.isalpha():
            char_lower = char.lower()  # Convert character to lowercase
            shifted_ascii = ord(char_lower) + inverse_key
            if char.islower():
                if shifted_ascii > ord('z'):
                    shifted_ascii -= 26
                elif shifted_ascii < ord('a'):
                    shifted_ascii += 26
            else:
                if shifted_ascii > ord('z'):
                    shifted_ascii -= 26
                elif shifted_ascii < ord('a'):
                    shifted_ascii += 26
            substituted_text += chr(shifted_ascii)
        else:
            # If the character is not an alphabet letter, keep it unchanged
            substituted_text += char
    return substituted_text

# ---------------------------------------------------------------



# -------------------------Transposition-------------------------

def transposition(text):
    return text[::-1]  # Reverses the string and returns it

# ---------------------------------------------------------------



# ----------------------------Product----------------------------

def productEncryption(text, key):
    cipher = ""
    for char in text:
        if char.isalpha():
            ascii_value = ord(char) - ord('a')  # Convert character to a number in the range 0 to 25
            encrypted_value = (ascii_value * key) % 26  # Apply the encryption formula
            cipher += chr(encrypted_value + ord('a'))  # Convert back to a character in the range 'a' to 'z'
        else:
            cipher += char  # Keep non-alphabetic characters unchanged
    return cipher

def productDecryption(cipher, key):
    inverse_key = 1
    for i in range(26):
        if (key * i) % 26 == 1:
            inverse_key = i
            break
    plaintext = ""
    for char in cipher:
        if char.isalpha():
            ascii_value = ord(char) - ord('a')  # Convert character to a number in the range 0 to 25
            decrypted_value = (ascii_value * inverse_key) % 26  # Apply the decryption formula
            plaintext += chr(decrypted_value + ord('a'))  # Convert back to a character in the range 'a' to 'z'
        else:
            plaintext += char  # Keep non-alphabetic characters unchanged
    return plaintext

# ---------------------------------------------------------------



def encrypt(text, key):

    # Substitution Encryption
    cipher_text = substitution(text, key)

    # Transposition Encryption
    cipher_text = transposition(cipher_text)

    # Product Encryption
    cipher_text = productEncryption(cipher_text, key);

    return cipher_text


def decrypt(cipher, key):

    # Product Decryption
    plain_text = productDecryption(cipher, key);

    # Transposition Decryption
    plain_text = transposition(plain_text)

    # Substitution Decryption
    plain_text = substitution(plain_text, key, inverse = True)

    return plain_text


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_valid_key(key):
    return gcd(key, 26) == 1

def get_valid_key():
    while True:
        key = int(input("Enter the key in integer [Do not use keys that have common factors with '26' other than '1'!]: "))
        if is_valid_key(key):
            return key
        else:
            print("Invalid key! Please enter a valid key.")

def main():
    plain_text = input("Enter the plaintext: ")

    key = get_valid_key()

    encrypted_text = encrypt(plain_text, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
