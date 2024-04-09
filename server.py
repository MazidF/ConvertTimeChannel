from socket import socket, gethostname, AF_INET, SOCK_STREAM
from threading import Thread
from time import time


def handle_client(client):
    message = ''
    client_was_sending = False

    while True:
        start_time = time()
        read = client.recv(1)

        if not read:
            break
        elif not client_was_sending:  # ignoring the first char
            client_was_sending = True
            continue

        now = time()
        if now - start_time >= 0.2:
            message += '1'
        else:
            message += '0'

    if message:
        result = ""
        for i in range(0, len(message), 8):
            result += chr(int(message[i:i + 8], 2))
        print(f'"{result}" received')


host, port = gethostname(), 3000

socket = socket(AF_INET, SOCK_STREAM)
socket.bind((host, port))
socket.listen(5)

print(f'Server is ready and listening on {host} ...')

while True:
    client_socket, address = socket.accept()
    print('Client connected: ', address)
    Thread(target=handle_client(client_socket)).start()
