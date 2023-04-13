	
	
import os
	
import base64

from Crypto.Cipher import AES

def encrypt(plain_text):
    # Generate a random 256-bit key
    key = os.urandom(32)

    # Pad the plain text to the nearest multiple of 16 bytes
    padded_plain_text = plain_text + b"\0" * (AES.block_size - len(plain_text) % AES.block_size)

    # Create an AES cipher object with the generated key
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt the padded plain text using the AES cipher
    cipher_text = cipher.encrypt(padded_plain_text)

    # Encode the key and cipher text as base64 strings for easy storage and transmission
    encoded_key = base64.b64encode(key).decode('utf-8')
    encoded_cipher_text = base64.b64encode(cipher_text).decode('utf-8')

    # Return the encoded key and cipher text
    return encoded_key, encoded_cipher_text
# Prompt the user for plain text input
plain_text = input("<<<<Enter the plain text to encrypt>>>>: ").encode('utf-8')

# Encrypt the plain text and print the key and cipher text
key, cipher_text = encrypt(plain_text)
print("<<<Key>>>:", key)
print("<<<Cipher text>>>:", cipher_text)
