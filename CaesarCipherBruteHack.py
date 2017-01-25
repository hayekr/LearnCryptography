#Caesar Cipher Brute-Force Hacker

message = 'GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key
for key in range(len(LETTERS)):
    # The blank translated string
    translated = ''

    # Run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # Get the number of the selected symbol
            num = num - key

            # Handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # Add the number's symbol at the end of the translated string
            translated = translated + LETTERS[num]
        else:
            # Just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # Display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, translated))