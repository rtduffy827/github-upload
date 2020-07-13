# Prime Number: Only divisible by itself and 1
#               (2, 3, 5, 7, 11, 13, 17, 19, ...)
# Composite Number: Can be factored into smaller integers
#                   (4 = 2 x 2, 6 = 2 x 3, 8 = 2 x 2 x 2, 9 = 3 x 3, ...)
# Unit: 1

# V1) Test all divisors from 2 through n-1 (skip 1 and n)
def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime

    for d in range (2, n):
        if n % d == 0:
            return False
    return True

# === Test Function ===
for n in range (1, 21):
    print(n, is_prime_v1(n))

import time
# ===== Time Function =====
t0 = time.time()
for n in range (1, 100000):
    is_prime_v1(n)
t1 = time.time()
print("Time required: ", t1 - t0)

# Next step: Reduce number of divisors we check
# 36 = 1 x 36   |   18 = 1 x 18                 | n = 1 x n
#    = 2 x 18   |      = 2 x 9                  |   = a x b
#    = 3 x 12   |      = 3 x 6                  |   = ...
#    = 4 x 9    |      = sqrt(18) x sqrt(18)    |   = sqrt(n) x sqrt(n) 
#    = 6 x 6    |      = 6 x 3                  |   = ...
#    = 9 x 4    |      = 9 x 2                  |   = b x a
#    = 12 x 3   |      = 18 x 1                 |   = n x 1
#    = 18 x 2   |                               |
#    = 36 x 1   |                               |

# V2)  Test all divisors from 2 through sqrt(N)

import math

def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime

    max_divisor =  math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n% d == 0:
            return False
    return True

# ====== Test Function =====
for n in range(1, 21):
    print(n, is_prime_v2(n))

# ===== Time Function =====
t0 = time.time()
for n in range (1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("Time required: ", t1 - t0)

def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # 1 is not prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n% 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

# ====== Test Function =====
for n in range(1, 21):
    print(n, is_prime_v3(n))

# ===== Time Function =====
t0 = time.time()
for n in range (1, 100000):
    is_prime_v3(n)
t1 = time.time()
print("Time required: ", t1 - t0)