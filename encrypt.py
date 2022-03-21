from modulo_arithmetic import square_and_multiply

N = 2667790481  # public key of my partner
e = 1217401139  # exponent of my partner
plaintext = "Hello Harpreet"  # plaintext which I will send


# Main Program
plaintext_chunks = []
for n in range(0, len(plaintext), 3):
    encoded_text = bytes(plaintext[n:n+3], "utf-8").hex()
    plaintext_chunks.append('0x' + encoded_text)
print("Plaintext in hexadecimal chunks:", plaintext_chunks)


ciphertext_chunks = []
for text in plaintext_chunks:
    cipher = square_and_multiply(int(text, 16), e, N)
    # cipher = pow(int(text, 16), e, N)
    ciphertext_chunks.append(cipher)

print("Ciphertext to send:", ciphertext_chunks)
