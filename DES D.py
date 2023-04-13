from Crypto.Cipher import DES
import base64

# Prompt the user for the encoded key and cipher text to decrypt
encoded_key = input("<<<<Enter the key>>>>: ")
encoded_cipher_text = input("<<<<Enter the cipher text>>>>: ")

# Decode the key and cipher text from base64 strings
key = base64.b64decode(encoded_key)
cipher_text = base64.b64decode(encoded_cipher_text)

# Create a DES cipher object with the key
cipher = DES.new(key, DES.MODE_ECB)

# Decrypt the cipher text using the DES cipher
padded_data = cipher.decrypt(cipher_text)

# Remove the padding from the decrypted data
data = padded_data.rstrip(b"\0")

# Print the decrypted data
print("Decrypted data>>>>>>", data.decode('utf-8'))
