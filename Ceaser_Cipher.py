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
  shifted_alphabet = alphabet[shift:] + alphabet[:shift]
  result = ""
  for char in text:
    if char.isalpha():
      # Check for uppercase and lowercase letters
      if char.isupper():
        index = alphabet.upper().index(char)
        new_char = shifted_alphabet.upper()[index]
      else:
        index = alphabet.index(char)
        new_char = shifted_alphabet[index]
    else:
      # Keep non-alphabetic characters unchanged
      new_char = char
    if mode == "encrypt":
      result += new_char
    else:
      result += shifted_alphabet[shifted_alphabet.index(new_char)]  # Decrypt by shifting back
  return result

# Get user input
message = input("Enter message: ")
shift = int(input("Enter shift value (positive for encryption, negative for decryption): "))
mode = input("Enter mode (encrypt/decrypt): ").lower()

# Check for valid mode
if mode not in ("encrypt", "decrypt"):
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

# Perform encryption or decryption
result = caesar_cipher(message, shift, mode)
print(f"{mode.title()}d message: {result}")