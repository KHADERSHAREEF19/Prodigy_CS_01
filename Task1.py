def encrypt(shift, text):
    result = ""
    for letter in text:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def decrypt(shift, text):
    result = ""
    for letter in text:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += letter
    return result

def main():
    while True:
        choice = input("Do you want to encrypt the text or decrypt the text? (E/D:) ")
        if choice.upper() == "E":
            text = input("Enter the text you want to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = encrypt(shift, text)
            print("Your Encrypted text is: ", encrypted)
        elif choice.upper() == "D":
            text = input("Enter the Text you want to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted = decrypt(shift, text)
            print("Your Decrypted text is: ", decrypted)
        else:
            print("Invalid input. Please try valid input.")
        cont = input("Do you want to continue? (Y/N): ")
        if cont.upper() != "Y":
            break
if __name__ == "__main__":
    main()