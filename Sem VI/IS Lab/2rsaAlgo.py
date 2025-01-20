# The RSA algorithm is a widely-used public-key encryption method that relies on the properties of prime numbers and modular arithmetic. Here's a detailed step-by-step explanation of the algorithm, followed by your Python code:

# ### Detailed Algorithm for RSA:

# 1. **Key Generation**:
#    - **Step 1**: Choose two distinct large prime numbers, `p` and `q`. These are secret and should be kept private.
#    - **Step 2**: Calculate the modulus `n` as the product of `p` and `q`, i.e.,  
#      \[ n = p \times q \]
#      The modulus `n` is used in both the public and private keys.
#    - **Step 3**: Compute Euler's totient function `φ(n)`, which is the number of integers less than `n` that are coprime with `n`. It is calculated as:  
#      \[ φ(n) = (p - 1) \times (q - 1) \]
#    - **Step 4**: Choose the public exponent `e`. This is an integer such that:  
#      \[ 1 < e < φ(n) \quad \text{and} \quad gcd(e, φ(n)) = 1 \]
#      (i.e., `e` should be coprime with `φ(n)`).
#    - **Step 5**: Calculate the private exponent `d`, which is the modular multiplicative inverse of `e` modulo `φ(n)`. This is done using the Extended Euclidean Algorithm:
#      \[ d \times e ≡ 1 \pmod{φ(n)} \]
#      The private key is `(d, n)`.

# 2. **Encryption**:
#    - **Step 1**: Convert the plaintext message `m` into a number `m` such that `0 < m < n`. 
#    - **Step 2**: Compute the ciphertext `c` using the public key `(e, n)`:
#      \[ c = m^e \pmod{n} \]
#    - The ciphertext `c` is the encrypted message.

# 3. **Decryption**:
#    - **Step 1**: Using the private key `(d, n)`, the recipient computes:
#      \[ m = c^d \pmod{n} \]
#    - The result `m` is the original plaintext message.

# ### Explanation of Your Python Code:

# 1. **Primality Check (`is_prime`)**:
#    The function checks if a number `n` is prime by testing divisibility from `2` to `sqrt(n)`.

# 2. **Random Prime Generation (`generate_prime_number`)**:
#    It repeatedly generates a random number between 100 and 1000 until it finds a prime number.

# 3. **Key Generation**:
#    - Two primes `p` and `q` are generated.
#    - The modulus `n` is calculated as `n = p * q`.
#    - Euler's totient `φ(n)` is computed as `(p - 1) * (q - 1)`.
#    - The public exponent `e` is chosen such that `gcd(e, φ(n)) = 1`.
#    - The private exponent `d` is computed as the modular inverse of `e` mod `φ(n)`.

# 4. **Encryption and Decryption**:
#    - The `encrypt` function calculates `c = m^e % n`, where `m` is the plaintext message.
#    - The `decrypt` function calculates `m = c^d % n`, where `c` is the ciphertext.

# 5. **Modular Inverse (`mod_inverse`)**:
#    - The extended Euclidean algorithm is used to find the modular inverse of `e` modulo `φ(n)`.

# 6. **Example**:
#    - A message is input by the user, encrypted with the public key `(e, n)`, and decrypted back with the private key `(d, n)`.

# The implementation shows the entire process from key generation to encryption and decryption, making it a hands-on demonstration of RSA encryption.

# Let me know if you need further clarifications or modifications!