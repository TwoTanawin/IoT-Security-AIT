import random
import math

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def FindPrime(s, t):
    primes = [i for i in range(s, t) if isPrime(i)]
    n = random.choice(primes)
    return n

def rand2Primes(s, t):
    p = FindPrime(s, t)
    q = FindPrime(s, t)
    return p, q

s = 0
t = 100

p, q = rand2Primes(s, t)

print(f"Prime number p: {p}")
print(f"Prime number q: {q}")
