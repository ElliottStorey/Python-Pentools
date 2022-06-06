import socket

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
sock.settimeout(5)


def scanPort(host, port):
    # connect_exc return error code instead of exception which is easy to handle
    if sock.connect_ex((host, port)):
        print("Port is down!")
    else:
        print("Port is up")

if __name__ == "__main__":
    host = input("Enter your IP: ")
    port = int(input("Enter the port: "))
    scanPort(host, port)