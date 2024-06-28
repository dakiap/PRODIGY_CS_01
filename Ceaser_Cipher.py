def caesar_cipher(text, shift, mode):
    """Encrypts or decrypts text using Caesar Cipher algorithm.

    Args:
        text: The text to encrypt or decrypt.
        shift: The number of positions to shift letters (positive for encryption, negative for decryption).
        mode: "encrypt" or "decrypt"

    Returns:
        The encrypted or decrypted text.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    if mode == "decrypt":
        shift = -shift  # For decryption, negate the shift value

    for char in text:
        if char.isalpha():
            # Check for uppercase and lowercase letters
            if char.isupper():
                start = ord('A')
                new_char = chr((ord(char) - start + shift) % 26 + start)
            else:
                start = ord('a')
                new_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            # Keep non-alphabetic characters unchanged
            new_char = char

        result += new_char

    return result

# Get user input
message = input("Enter message: ")
shift = int(input("Enter shift value : "))
mode = input("Enter mode (encrypt/decrypt): ").lower()

# Check for valid mode
if mode not in ("encrypt", "decrypt"):
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
    exit()

# Perform encryption or decryption
result = caesar_cipher(message, shift, mode)
print(f"{mode.title()}ed message: {result}")
