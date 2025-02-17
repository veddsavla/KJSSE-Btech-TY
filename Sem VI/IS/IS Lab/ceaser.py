def caesar_cipher(text, shift):
    shift = shift % 26
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += new_char
        else:
            result += char
    
    return result

def main():
    try:
        text = input("Enter the text to be encrypted: ")
        shift = int(input("Enter the shift value: "))
        
        encrypted_text = caesar_cipher(text, shift)
        print(f"Encrypted Text: {encrypted_text}")
        
        decrypted_text = caesar_cipher(encrypted_text, -shift)
        print(f"Decrypted Text: {decrypted_text}")
        
    except ValueError:
        print("Error: Please enter a valid integer for the shift value.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()