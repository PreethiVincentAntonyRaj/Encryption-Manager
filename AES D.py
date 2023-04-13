

import base64
 
import binascii
	

from Crypto.Cipher import AES



def decrypt(key, cipher_text):
    try:
        # Decode the key and cipher text from base64 strings
        decoded_key = base64.b64decode(key)
        decoded_cipher_text = base64.b64decode(cipher_text)

        # Create an AES cipher object with the decoded key
        cipher = AES.new(decoded_key, AES.MODE_ECB)

        # Decrypt the cipher text using the AES cipher
        padded_plain_text = cipher.decrypt(decoded_cipher_text)

        # Remove any padding from the plain text
        plain_text = padded_plain_text.rstrip(b"\0")

        # Return the original plain text
        return plain_text.decode('utf-8')

    except (binascii.Error, ValueError) as e:
        print("Error:", e)
        return None

# Prompt the user for key and cipher text input
key = input("<<<<Enter the key>>>>: ")
cipher_text = input("<<<<Enter the cipher text>>>>: ")

# Decrypt the cipher text using the key and print the original plain text
plain_text = decrypt(key, cipher_text)

if plain_text:
    print("Plain text>>>>>>", plain_text)
else:
    print("^&^Decryption failed^&^.")
