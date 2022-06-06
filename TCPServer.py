import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()
print(f'Host Name: {host}')

port = 8081
print(f'Port: {port}')

server.bind((host, port))

server.listen(5)
print('Server Is Listening')

while True:
    client, address = server.accept()
    print(f'Client: {str(address)}')

    msg = 'Beep Boop Beep'
    client.send(msg.encode('ascii'))
    client.close()