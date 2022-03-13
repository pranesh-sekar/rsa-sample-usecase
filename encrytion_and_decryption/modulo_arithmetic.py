def square_and_multiply(num, e, modulo):
    exp = bin(e)
    value = num
    for i in range(3, len(exp)):
        value = (value * value) % modulo
        if(exp[i:i+1] == '1'):
            value = (value * num) % modulo
    return value


def multiplicative_inverse(a, m):
    for i in range(1, m):
        if (m*i + 1) % a == 0:
            return (m*i + 1) // a
    return None


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True
