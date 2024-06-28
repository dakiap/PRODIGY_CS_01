# PRODIGY_CS_01

**Caesar Cipher Encryption and Decryption**

This Python program implements the Caesar Cipher algorithm for both encryption and decryption of text messages. It provides a user-friendly interface to enter the message, choose the shift value, and select the desired operation (encryption or decryption).

**Features:**

- **Encryption and Decryption:** Encrypts plain text messages using the Caesar Cipher and decrypts ciphertext back to the original message.
- **User Input:** Prompts the user to enter the message to be processed.
- **Shift Value:** Allows the user to specify the number of positions to shift letters in the alphabet (positive for encryption, negative for decryption).
- **Mode Selection:** Enables the user to choose between encryption and decryption modes.
- **Error Handling:** Checks for invalid mode input (other than "encrypt" or "decrypt") and exits gracefully with an informative message.

**How to Use:**

1. **Clone or Download the Repository:** Clone the repository using Git or download the source code files.
2. **Run the Script:** Open a terminal or command prompt, navigate to the project directory, and execute the Python script using `python caesar_cipher.py` (replace `caesar_cipher.py` with the actual filename if different).
3. **User Input:** Follow the on-screen prompts to enter the message, shift value, and desired mode (encrypt or decrypt).

**Example Usage:**

```
Enter message: Hello, world!
Enter shift value (positive for encryption, negative for decryption): 3
Enter mode (encrypt/decrypt): encrypt

Encrypted message: Khoor, zruog!
```

**How it Works:**

The program utilizes the Caesar Cipher algorithm, a simple substitution cipher where each letter in the message is shifted a fixed number of positions down the alphabet during encryption and back up during decryption. The `caesar_cipher` function handles the core logic of letter shifting and mode selection.

**Further Enhancements (Optional):**

- **GUI Implementation:** Create a graphical user interface (GUI) for a more user-friendly experience.
- **Advanced Features:** Explore extensions like handling punctuation characters or different alphabet sizes (e.g., including uppercase and lowercase or other languages).

**Feel free to contribute to this project by creating pull requests for improvements or bug fixes!**
