import modulo_arithmetic as modulo_arithmetic


N = 2667790481  # public key of my partner
e = 1217401139  # exponent of my partner

# signed text from partner
signed_text_chunks = [2288450091, 2603155990, 341728729, 1086428306, 607685959]

# Main Program
signature = ""
for chunk in signed_text_chunks:
    text_as_integer = modulo_arithmetic.square_and_multiply(chunk, e, N)
    text_as_hex = hex(text_as_integer)
    text = bytes.fromhex(text_as_hex.removeprefix('0x')).decode('utf-8')
    signature += text

print("Signature received:", signature)
