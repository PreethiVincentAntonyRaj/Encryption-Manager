from Crypto.Cipher import DES
import base64
import os

# Prompt the user for data to encrypt
data = input("<<<<Enter data to encrypt>>>>: ").encode('utf-8')

# Generate a random 8-byte key for DES encryption
key = os.urandom(8)

# Pad the data to a multiple of 8 bytes (the block size of DES)
padded_data = data + b"\0" * (DES.block_size - len(data) % DES.block_size)

# Create a DES cipher object with the key
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt the padded data using the DES cipher
cipher_text = cipher.encrypt(padded_data)

# Encode the key and cipher text as base64 strings for easy storage and transmission
encoded_key = base64.b64encode(key).decode('utf-8')
encoded_cipher_text = base64.b64encode(cipher_text).decode('utf-8')

# Print the encoded key and cipher text for decryption
print("Use the following key and cipher text for decryption:")
print("<<<<Key>>>>:", encoded_key)
print("<<<<Cipher text>>>>:", encoded_cipher_text)
