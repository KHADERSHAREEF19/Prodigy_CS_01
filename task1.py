def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            ciphertext.append(chr(shifted))
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (positive integer): "))
    
    encrypted_message = caesar_cipher_encrypt(message, shift)
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    
    print("\nOriginal message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
