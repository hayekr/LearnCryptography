# Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in the cipherText to the string
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard
    pyperclip.copy(ciphertext)


if __name__ == '__main__':
    def encryptMessage(key, message):
        # Each string in cipherText represents a column in the grid.
        ciphertext = [''] * key

        # Loop through each column in ciphertext
        for col in range(key):
            pointer = col

            # Keep looping until pointer goes past the length of the message
            while pointer < len(message):
                # Place the character at pointer in message at the end of the
                # current column in the ciphertext list
                ciphertext[col] += message[pointer]

                # Move the pointer over
                pointer += key

        # Convert the ciphertext list into a single string value and return it
                return ''.join(ciphertext)

# If transpostion Encrypt.py is run (instead of imported as module) call
# the main() function
if __name__ == '__main__':
    main()
