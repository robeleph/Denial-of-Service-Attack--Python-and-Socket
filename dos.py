import socket
from random import _urandom

def main():
    ip_address = "127.0.0.1"
    port = 3000
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        sock.connect((ip_address, port))
        sock.send(_urandom(1024))

if __name__ == "__main__": main()