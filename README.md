# PRODIGY_CS_01
Caesar Cipher Implementation for Internship Task.
## Description
This repository contains a Python implementation of the Caesar cipher algorithm, which is a simple encryption technique. The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 1, 'A' would become 'B', 'B' would become 'C', and so on.

## Features
- **Encrypt messages**: Convert plaintext into ciphertext using a specified shift value.
- **Decrypt messages**: Convert ciphertext back into plaintext using the same shift value.
- Handles both uppercase and lowercase letters.
- Non-alphabetic characters remain unchanged.

## How to Run
1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).
2. Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/<your_username>/prodigy_CS_1.git
3. #Navigate to the project directory:
   cd prodigy_CS_1
4. #Run the program with Python:
   python caesar_cipher.py
5. Follow the prompts to encrypt or decrypt a message. Enter your message and the desired shift value.

## Example Usage
To encrypt a message:

Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message (or 'exit' to quit): encrypt
Enter the message: Hello World!
Enter the shift value (0-25): 3
Encrypted message: Khoor Zruog!

To decrypt a message:

Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message (or 'exit' to quit): decrypt
Enter the message: Khoor Zruog!
Enter the shift value (0-25): 3
Decrypted message: Hello World!


