# public key
N = 2667790481
# exponent
e = 1217401139


# plaintext
plaintext = 50

cipher = (plaintext ** e) * N

# Return the cipher
print(cipher)
