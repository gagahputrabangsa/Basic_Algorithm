# XOR Operator Example in Python

def xor_integers(a, b):
    """Performs XOR operation on two integers."""
    return a ^ b
def xor_booleans(a, b):
    """Performs XOR operation on two boolean values."""
    return a ^ b

def xor_binary_strings(bin1, bin2):
    """Performs XOR operation on two binary strings."""
    # Convert binary strings to integers, XOR them, then convert back to binary string
    xor_result = int(bin1, 2) ^ int(bin2, 2)
    return bin(xor_result)[2:].zfill(max(len(bin1), len(bin2)))


