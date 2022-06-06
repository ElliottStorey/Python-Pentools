import socket

def banner(ip, port):
    sock = socket.socket()
    try:
        sock.connect((ip, port))
        sock.settimeout(5) # set timeout for 5 seconds
        print(str(sock.recv(1024)))
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    ip = input('Enter your ip: ')
    port = int(input('Enter the port: '))
    banner(ip, port)