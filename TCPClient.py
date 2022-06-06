import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()
print(f'Host Name: {host}')

port = 8081
print(f'Port: {port}')

client.connect((host, port))

# allow maximum data size received from the server
msg = client.recv(1024)

client.close()

print(f'Server: {msg.decode("ascii")}')