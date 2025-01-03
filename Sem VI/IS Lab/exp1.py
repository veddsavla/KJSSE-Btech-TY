# Playfair Cipher Algorithm

# 1. Define the key
#    - This is the key provided by the user for encryption.
#    - Example: "KEYWORD"

# 2. Standardize the key
#    - Convert the key to uppercase or lowercase for consistency.
#    - Remove duplicate letters while maintaining the order.
#    - Combine 'I' and 'J' as one character (usually represented as 'I').

# 3. Create the 5x5 Playfair matrix
#    - Start by filling the matrix with the key's letters (without duplicates).
#    - Fill the remaining spaces with the rest of the alphabet (excluding the letters in the key and treating 'I'/'J' as one).
#    - Ensure the matrix contains exactly 25 unique characters.

# 4. Prepare the plaintext
#    - Standardize the plaintext (uppercase or lowercase).
#    - Remove spaces and non-alphabet characters (optional based on your rules).
#    - Divide the plaintext into pairs of two letters.
#       * If a pair contains duplicate letters (e.g., 'AA'), insert a filler (e.g., 'AX').
#       * If there's an odd number of letters, append a filler to the last letter.

# 5. Encrypt each pair
#    - Apply the following rules to each pair of letters:
#       a. If both letters are in the same row, shift each one to the right (wrap around if needed).
#       b. If both letters are in the same column, shift each one downward (wrap around if needed).
#       c. If the letters form a rectangle, replace them with the letters at the opposite corners of the rectangle.

# 6. Combine encrypted pairs
#    - Concatenate all the encrypted pairs to form the final ciphertext.

# 7. (Optional) Decryption rules
#    - Reverse the encryption steps:
#       a. For the same row, shift each letter to the left.
#       b. For the same column, shift each letter upward.
#       c. For a rectangle, swap the letters at the opposite corners of the rectangle.

# 8. Handle edge cases (optional)
#    - Define rules for non-alphabet characters in the plaintext.
#    - Specify how to treat filler letters during decryption.