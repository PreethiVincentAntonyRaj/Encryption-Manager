

	
from Crypto.PublicKey import RSA

from Crypto.Cipher import PKCS1_OAEP
 	
import base64

# Prompt the user for the encoded public and private keys and cipher text

encoded_private_key = input("<<<<Enter the private key>>>>: ")
encoded_cipher_text = input("<<<<Enter the cipher text>>>>: ")

# Decode the keys and cipher text from base64 strings

private_key = RSA.import_key(base64.b64decode(encoded_private_key))
cipher_text = base64.b64decode(encoded_cipher_text)

# Create a cipher object with the private key and use PKCS1_OAEP padding
cipher = PKCS1_OAEP.new(private_key)

# Decrypt the cipher text using the cipher
data = cipher.decrypt(cipher_text)

# Print the decrypted data
print("Decrypted data>>>>", data.decode('utf-8'))
