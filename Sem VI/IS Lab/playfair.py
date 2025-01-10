def standardize_key(key):
    # single case
    key = key.upper()

    # combine i and j
    key = key.replace("J", "I")

    # removing duplicate letters + maintaining order
    standardized_key = ""
    for char in key:
        if char not in standardized_key and char.isalpha():  # ensuring its a letter
            standardized_key += char

    return standardized_key


def playfair_matrix(key):

    # key = standardize_key(key)
    alphabet = "ABCDEFGHIKLMNOPQRTSUVWXYZ"  # no J

    matrix = []
    for char in key:  # adding std_key to the matrix
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:  # adding remainig letters to the matrix
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = []
    for i in range(5):
        playfair_matrix.append(
            matrix[i * 5 : (i + 1) * 5]
        )  # matrix[0:5],  matrix[5:10], matrix[10:15] and so on..

    return playfair_matrix


def plaintext_pairs(plaintext):

    plaintext = plaintext.upper()
    plaintext_paired = []
    i = 0

    while i < len(plaintext):
        letter1 = plaintext[i]
        if i + 1 < len(plaintext):
            letter2 = plaintext[i + 1]
            if letter1 == letter2:
                plaintext_paired.append(letter1 + "X")
                plaintext_paired.append(letter2 + "X")
                i = i + 2
            else:
                plaintext_paired.append(letter1 + letter2)
                i = i + 2
        else:
            plaintext_paired.append(letter1 + "X")
            i = i + 1

    return plaintext_paired


def encrypt(letter1, letter2, pmatrix):
    encrypted_pair = ""
    row1, col1, row2, col2 = -1, -1, -1, -1
    # Find positions of the two letters
    for i, row in enumerate(pmatrix):
        if letter1 in row:
            row1, col1 = i, row.index(letter1)
        if letter2 in row:
            row2, col2 = i, row.index(letter2)

    # Same row
    if row1 == row2:
        encrypted_pair = pmatrix[row1][(col1 + 1) % 5] + pmatrix[row2][(col2 + 1) % 5]

    # Same column
    elif col1 == col2:
        encrypted_pair = pmatrix[(row1 + 1) % 5][col1] + pmatrix[(row2 + 1) % 5][col2]

    # Rectangle rule
    else:
        encrypted_pair = pmatrix[row1][col2] + pmatrix[row2][col1]

    return encrypted_pair


# key
key = input("Enter the  key (e.g., 'KEYWORD'): ")
skey = standardize_key(key)
print(f"The standardized key  is: {skey}")

# making matrix 5x5
pmatrix = playfair_matrix(skey)

# print(pmatrix)
print("The Playfair matrix is:")  # printing the matrix w/o [,]
for row in pmatrix:
    print(" ".join(row))

# taking the plaintext from user
plaintext = input("Enter the  plaintext: ")
# print({plaintext})

# dividing the plaintext into pairs of two letters:
prepared_text = plaintext_pairs(plaintext)
print(prepared_text)

# Encrypting the prepared plaintext pairs
encrypted_text = ""
for pair in prepared_text:
    letter1, letter2 = pair[0], pair[1]  # Extract each pair of letters
    encrypted_text += encrypt(
        letter1, letter2, pmatrix
    )  # Encrypt the pair and append to the result

print("The encrypted text is:", encrypted_text)
