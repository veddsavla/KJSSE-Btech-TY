import math
import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(
        2, int(math.sqrt(n)) + 1
    ):  # checking for prime number till sqrt of n
        if n % i == 0:
            return False  # not prime number
    return True


def generate_prime_number():
    while True:
        # Generate a random number between 100 and 1000
        num = random.randint(100, 1000)
        if is_prime(num):
            return num


# Generate two distinct prime numbers
p = generate_prime_number()
q = generate_prime_number()

# Make sure p and q are different
while p == q:
    q = generate_prime_number()

print(f"First prime (p): {p}")
print(f"Second prime (q): {q}")

n = p * q
print(f"\nModulus (n = p * q): {n}")

# Calculate Euler's totient function φ(n) = (p-1) × (q-1)
phi = (p - 1) * (q - 1)
print(f"\nEuler's totient φ(n) = (p-1) × (q-1): {phi}")


# Function to calculate GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        # a,b=b,a%b
        temp = b
        b = a % b
        a = temp
    return a


# Choose public exponent e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
def choose_e(phi):
    # Common choice for e is 65537, as it's a prime number and computationally efficient
    e = 65537
    # If 65537 is too large for our phi, we'll find a smaller value
    if e >= phi:
        for i in range(3, phi, 2):
            if gcd(i, phi) == 1:
                return i
    return e


# Calculate public exponent e
e = choose_e(phi)
print(f"\nPublic exponent (e): {e}")
print("This e is coprime with φ(n) and 1 < e < φ(n)")
