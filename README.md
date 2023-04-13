ENCRYPTION MANAGER
The Encryption Manager is a software tool that operates through a command-line interface and facilitates encryption and decryption operations utilising a range of encryption algorithms, including but not limited to AES, DES, and RSA. The aforementioned tool facilitates the encryption of data provided by the user and offers the user the choice to preserve the encoded data as base64 strings, thereby simplifying the process of storage and transmission.

Installation

To use Encryption Manager, follow these steps:
    Clone this repository to your local machine.
    Install the required dependencies by running pip install -r requirements.txt.
    Run the EM.py file using the command python3 EM.py to start the tool.
    
    Usage

Encryption Manager provides the following encryption and decryption options:
AES Encryption

To encrypt data using AES, select option 1 from the main menu and follow the prompts to enter the plaintext and encryption key.
AES Decryption

To decrypt data using AES, select option 2 from the main menu and follow the prompts to enter the ciphertext and decryption key.
DES Encryption

To encrypt data using DES, select option 3 from the main menu and follow the prompts to enter the plaintext and encryption key.
DES Decryption

To decrypt data using DES, select option 4 from the main menu and follow the prompts to enter the ciphertext and decryption key.
RSA Encryption

To encrypt data using RSA, select option 5 from the main menu and follow the prompts to enter the plaintext. The tool will generate a new RSA key pair with a key length of 2048 bits and use the public key for encryption.
RSA Decryption

To decrypt data using RSA, select option 6 from the main menu and follow the prompts to enter the ciphertext and the private key.
License

Encryption Manager is released under the MIT License.
