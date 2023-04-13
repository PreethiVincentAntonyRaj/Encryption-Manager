from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Prompt the user for data to encrypt
data = input("<<<<Enter data to encrypt>>>> ").encode('utf-8')

# Generate a new RSA key pair with a key length of 2048 bits
key = RSA.generate(2048)

# Get the public key for encryption
public_key = key.publickey()

# Create a cipher object with the public key and use PKCS1_OAEP padding
cipher = PKCS1_OAEP.new(public_key)

# Encrypt the data using the cipher
cipher_text = cipher.encrypt(data)

# Encode the public and private keys and cipher text as base64 strings for easy storage and transmission
encoded_public_key = base64.b64encode(public_key.export_key()).decode('utf-8')
encoded_private_key = base64.b64encode(key.export_key()).decode('utf-8')
encoded_cipher_text = base64.b64encode(cipher_text).decode('utf-8')

# Print the encoded keys and cipher text for decryption
print("Use the following keys and cipher text for decryption:")
print("<<Public key>>:", encoded_public_key)
print("<<Private key>>:", encoded_private_key)
print("<<Cipher text>>:", encoded_cipher_text)
