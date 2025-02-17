import math
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_number():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num



# Generate two distinct primes
p = generate_prime_number()
q = generate_prime_number()
while p == q:
    q = generate_prime_number()

print(f"First prime (p): {p}")
print(f"Second prime (q): {q}")

n = p * q
print(f"\nModulus (n = p * q): {n}")

phi = (p - 1) * (q - 1)
print(f"\nEuler's totient φ(n): {phi}")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def choose_e(phi):
    e = 65537
    if e >= phi:
        for i in range(3, phi, 2):
            if gcd(i, phi) == 1:
                return i
    return e

e = choose_e(phi)
print(f"\nPublic exponent (e): {e}")

def mod_inverse(a, m):
    old_r, r = a, m
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if old_r != 1:
        return None  # Inverse doesn't exist
    return old_s % m

d = mod_inverse(e, phi)
print(f"Private exponent (d): {d}")

def encrypt(message_str, e, n):
    # Convert message to bytes
    bytes_message = message_str.encode('utf-8')
    m = int.from_bytes(bytes_message, byteorder='big')
    if m >= n:
        raise ValueError("Message is too long to encrypt with the current modulus.")
    c = pow(m, e, n)
    return c

def decrypt(c, d, n):
    m = pow(c, d, n)
    # Convert integer back to bytes
    byte_length = (m.bit_length() + 7) // 8
    bytes_message = m.to_bytes(byte_length, byteorder='big')
    return bytes_message.decode('utf-8')

# Example usage
try:
    message = input("\nEnter a message to encrypt: ")
    ciphertext = encrypt(message, e, n)
    print(f"\nEncrypted ciphertext (c = m^e mod n): {ciphertext}")

    decrypted_message = decrypt(ciphertext, d, n)
    print(f"Decrypted message: {decrypted_message}")
except ValueError as e:
    print(f"Error: {e}")