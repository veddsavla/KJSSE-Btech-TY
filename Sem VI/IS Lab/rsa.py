import math
import random

# Check if a number is prime by testing divisibility up to its square root
# Input: n - number to test for primality 
# Output: True if n is prime, False otherwise
# Method: Tests divisibility by all integers from 2 to sqrt(n)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random prime number between 100 and 1000
# Output: A random prime number in range [100,1000]
# Method: Repeatedly generates random numbers until a prime is found
def generate_prime_number():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num

# Generate two distinct prime numbers p and q for RSA key generation
p = generate_prime_number()
q = generate_prime_number()
while p == q:  # Ensure p and q are different
    q = generate_prime_number()

print(f"Generated prime numbers: p = {p}, q = {q}")

# Calculate n = p * q (modulus for public and private keys)
# n is used as the modulus for both the public and private keys
n = p * q
print(f"n = p * q = {n}")

# Calculate Euler's totient function φ(n) = (p-1)(q-1)
# The totient function counts numbers up to n that are coprime to n
phi = (p - 1) * (q - 1)
print(f"φ(n) = {phi}")

# Calculate Greatest Common Divisor using Euclidean algorithm
# Input: a,b - two numbers to find GCD of
# Output: Greatest Common Divisor of a and b
# Method: Uses Euclidean algorithm with repeated division
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Choose public key exponent e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
# Input: phi - Euler's totient of n
# Output: Public key exponent e
# Method: Tests odd numbers until finding one coprime with phi
def choose_e(phi):
    for e in range(3, phi, 2):  # Start with odd numbers for efficiency
        if gcd(e, phi) == 1:
            return e

e = choose_e(phi)
print(f"Public key (e) = {e}")

# Calculate private key d using Extended Euclidean Algorithm
# Input: e - public exponent, phi - Euler's totient
# Output: Private key d, the modular multiplicative inverse of e mod phi
# Method: Uses extended Euclidean algorithm to find modular inverse
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:  # Ensure d is positive
        d += phi
    return d

d = mod_inverse(e, phi)
print(f"Private key (d) = {d}")

# Encryption function: c = m^e mod n
# Input: message - plaintext number, e - public exponent, n - modulus
# Output: Encrypted ciphertext
# Method: Uses modular exponentiation
def encrypt(message, e, n):
    return pow(message, e, n)

# Decryption function: m = c^d mod n
# Input: ciphertext - encrypted number, d - private key, n - modulus
# Output: Decrypted plaintext
# Method: Uses modular exponentiation
def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# Example usage with user input - demonstrates encryption/decryption process
try:
    message = int(input("Enter a number to encrypt (smaller than n): "))
    if message >= n:
        raise ValueError("Message must be smaller than n")
    
    print(f"\nOriginal message: {message}")

    # Encrypt the message using public key (e,n)
    ciphertext = encrypt(message, e, n)
    print(f"Encrypted message: {ciphertext}")

    # Decrypt the ciphertext using private key (d,n)
    decrypted_message = decrypt(ciphertext, d, n)
    print(f"Decrypted message: {decrypted_message}")

except ValueError as e:
    print(f"Error: {e}")
    print("Please run the program again with a valid input")

# Display the final public and private key pairs for verification
print("\nVerifying the keys:")
print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")
