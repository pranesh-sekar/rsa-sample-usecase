import math
import random
from modulo_arithmetic import is_prime, gcd

e = 65537  # my exponent


def generate_prime(maximum_value, minumum_value=3):
    num = random.randint(minumum_value, maximum_value)
    if is_prime(num):
        return num
    else:
        return generate_prime(maximum_value, minumum_value)


def get_two_primes_for_rsa():
    p = generate_prime(maximum_value=65536)
    q = generate_prime(maximum_value=65536)
    phi_of_n = (p-1) * (q-1)
    if gcd(e, phi_of_n) == 1:
        print("p =", p)
        print("q =", q)
        return
    else:
        return get_two_primes_for_rsa()


# Main Program
get_two_primes_for_rsa()
