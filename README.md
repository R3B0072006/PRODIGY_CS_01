# PRODIGY_CS_01
Caesar Cipher Implementation for Internship Task.
## Description
This repository contains a Python implementation of the Caesar cipher algorithm, which is a simple encryption technique. The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 1, 'A' would become 'B', 'B' would become 'C', and so on.

## Features
1. **Encrypt messages**: Convert plaintext into ciphertext using a specified shift value.
2. **Decrypt messages**: Convert ciphertext back into plaintext using the same shift value.
3. Handles both uppercase and lowercase letters.
4. Non-alphabetic characters remain unchanged.

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




# PRODIGY_CS_03
Password Complexity Checker
## Description
This tool evaluates the strength of a password based on several criteria, such as length, the presence of uppercase and lowercase letters, numbers, and special characters. It provides real-time feedback to users about the strength of their password and suggests areas for improvement to enhance password security. The tool categorizes the password as "Weak," "Medium," or "Strong," helping users choose more secure passwords.

## Features
1. Length Check: Ensures that the password meets a minimum length requirement (e.g., 8 characters).
2. Character Variety: Verifies that the password includes a mix of uppercase letters, lowercase letters, digits, and special characters.
3. Real-Time Feedback: Users receive instant feedback on their password strength, with clear categories like "Weak," "Medium," or "Strong."
4. Strength Rating: Based on the above checks, the tool rates the password as "Weak," "Medium," or "Strong."

## How to Run
1. Input the Password: The tool prompts the user to input a password.
2. Password Evaluation: The tool checks if the password meets the following criteria:
3. Length: Minimum 8 characters
4. Includes uppercase and lowercase letters
5. Includes numbers
6. Includes at least one special character (e.g., @, #, !, etc.)

## Feedback
The tool provides feedback on the strength of the password and suggests improvements.

## Example Usage
Example 1
Input: Password123!
Result: Password strength: Strong
Example 2
Input: pass123
Result: Password strength: Medium
Example 3
Input: 12345
Result: Password strength: Weak





