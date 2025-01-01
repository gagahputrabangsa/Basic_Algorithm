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

# run
if __name__ == "__main__":
    num1 = 12  # 1100 in binary
    num2 = 9   # 1001 in binary
    print(f"XOR of {num1} and {num2} is: {xor_integers(num1, num2)}")

   
 # Boolean XOR
    bool1 = True
    bool2 = False
    print(f"XOR of {bool1} and {bool2} is: {xor_booleans(bool1, bool2)}")

  
  # Binary String XOR
    bin1 = "1101"
    bin2 = "1011"
    print(f"XOR of binary strings '{bin1}' and '{bin2}' is: {xor_binary_strings(bin1, bin2)}")
