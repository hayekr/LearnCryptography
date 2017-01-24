# CaesarCipher

#import pyperclip

# The string to be encrypted/decrypted
message = 'KQEUCQIYDC'

# The encryption/decryption key
key = 16

# Tell the program to encrypt or decrypt
mode = 'decrypt'  # set to 'encrypt' or 'decrypt'

# Every possible letter(s) that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYXZ'

# Stores the encrypted/decrypted message
translated = ''

# Capitalize the string in the message
message = message.upper()

# Run the encryption/decryption program on each symbol in the string
for symbol in message:
    if symbol in LETTERS:
        # Get the encrypted/decrypted symbol for this number
        num = LETTERS.find(symbol)

        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle the wrap-around if the number is greater than the length of LETTER or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # Add encrypted/decrypted number's symbol at the end of the translation
        translated = translated + LETTERS[num]

    else:
        # Just add the symbol without encrypting or decrypting
        translated = translated + symbol

# Print the encrypted/decrypted string
print(translated)

# Copy the translated string to the clipboard
#pyperclip.copy(translated)