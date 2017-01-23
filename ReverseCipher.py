# Reverse Cipher
# To decrypt Copy and paste encrypted message into the message variable.

message = 'I need to be in reverse, can you encrypt me'

translated = ''

i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)