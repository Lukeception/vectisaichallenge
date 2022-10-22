
#%%
test_primes =  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
    419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
    607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
    661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
    739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
    811, 821, 823, 827, 829, 839, 853, 857, 859]

#%%
# Only works is the prime_list is complete for all primes up to sqrt(p).
def is_prime(p, prime_list):
    m = (p ** 0.5)
    for i in prime_list:
        if i > m or i == 0:
            break
        elif p % i == 0:
            return False
    return True


# Generates a list of n primes and their sum
def primes(n):
    primes = [2]
    s = 2
    k = 1
    while len(primes) < n:
        p = k * 2 + 1
        if is_prime(p, primes):
            primes.append(p)
            s += p
        k += 1
    return primes, s


# Returns largest prime factor of p
def largest_p_factor(p, prime_list):
    f = 1
    for i in prime_list:
        if i > p:
            return f
        elif p % i == 0:
            f = i


# %%
# Calculate primes up to 1000003
primes, s = primes(100003)

# %%
# Get last three digits
l = int(str(s)[-3:])

# %%
# find largest prime factor of l
l_p = largest_p_factor(l, primes)

# %%
print(l_p)