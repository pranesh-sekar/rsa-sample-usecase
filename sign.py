import modulo_arithmetic as modulo_arithmetic

N = 269419387  # public key of myself
d = 163267073  # d of myself
original_text = "Pranesh Sekar"  # signature which I will send


# Main Program
original_text_chunks = []
for n in range(0, len(original_text), 3):
    encoded_text = bytes(original_text[n:n+3], "utf-8").hex()
    original_text_chunks.append('0x' + encoded_text)
print("Original Text in hexadecimal chunks:", original_text_chunks)


signed_text_chunks = []
for text in original_text_chunks:
    signed_text = modulo_arithmetic.square_and_multiply(int(text, 16), d, N)
    signed_text_chunks.append(signed_text)

print("Signed Text to send:", signed_text_chunks)
