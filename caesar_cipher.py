def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Encrypt/Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt/Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result

def main():
    while True:
        mode = input("Type 'encrypt' to encrypt a message or 'decrypt' to decrypt a message (or 'exit' to quit): ").lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (0-25): "))
        
        if mode == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, mode)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher(message, shift, mode)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
