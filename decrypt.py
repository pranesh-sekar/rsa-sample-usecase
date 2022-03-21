import modulo_arithmetic as modulo_arithmetic

# my prime numbers
p = 16411
q = 16417

N = p * q  # 269419387
phi_of_N = (p-1) * (q - 1)  # 269386560


e = 65537  # my exponent
d = modulo_arithmetic.multiplicative_inverse(e, phi_of_N)  # 163267073

# ciphertext from partner
ciphertext_chunks = [267560136, 110706760, 162709083, 223920506, 76567147]

# Main Program
plaintext = ""
for chunk in ciphertext_chunks:
    text_as_integer = modulo_arithmetic.square_and_multiply(chunk, d, N)
    text_as_hex = hex(text_as_integer)
    text = bytes.fromhex(text_as_hex.removeprefix('0x')).decode('utf-8')
    plaintext += text

print("Plaintext received:", plaintext)
