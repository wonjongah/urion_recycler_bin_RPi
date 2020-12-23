import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.35.148', 7777)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)

    print('received {} bytes from {}'.format(len(data), address))
    if data.decode() == 'hijonga~~~~':
        print(data.decode())