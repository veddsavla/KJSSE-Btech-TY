# Algorithm: Caesar Cipher Encryption

# Step 1: Start
# - Input the plaintext (P) and the shift key (k).
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
print(f"The plaintext  is: {plaintext}")
print(f"The key  is: {key}")

# Step 2: Iterate through each character in the plaintext (P):
#   - Check if the character is an uppercase letter:
#     a. Calculate the new character using the formula:
#        Ci = (Pi - 65 + k) % 26 + 65
#        Where:
#          - Pi is the ASCII value of the current character.
#          - 65 is the ASCII value of 'A' (used to normalize the range of uppercase letters).
#     b. Append the resulting character to the ciphertext.

#   - Check if the character is a lowercase letter:
#     a. Calculate the new character using the formula:
#        Ci = (Pi - 97 + k) % 26 + 97
#        Where:
#          - Pi is the ASCII value of the current character.
#          - 97 is the ASCII value of 'a' (used to normalize the range of lowercase letters).
#     b. Append the resulting character to the ciphertext.

#   - Check if the character is non-alphabetic:
#     a. Append the character directly to the ciphertext without applying any encryption.

# Step 3: Output the resulting ciphertext (C).
