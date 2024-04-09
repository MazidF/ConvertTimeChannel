import random
import string
from time import sleep
from socket import socket, gethostname, AF_INET, SOCK_STREAM

host, port = gethostname(), 3000

socket = socket(AF_INET, SOCK_STREAM)
socket.connect((host, port))

print('Socket is connected')

message = input('Enter your message: ')

print(f'Sending {message} ...')

chars = ''
for char in message:
    chars += format(ord(char), '08b')

socket.send(b'$')  # sending the first byte

for char in chars:
    print(char, end=', ')
    if char == '0':
        sleep(0.1)
    else:  # char == '1'
        sleep(0.2)

    random_char = random.choice(string.ascii_letters)
    byte = char.encode('utf-8')
    socket.send(byte)

print('')
print('The message was sent to the server')
socket.close()
