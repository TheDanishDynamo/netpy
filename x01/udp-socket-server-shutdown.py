import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

server = socket.socket(socket.AF_INET,   # Internet
                     socket.SOCK_DGRAM)  # UDP

server.bind((UDP_IP, UDP_PORT))

while True:
    print "."
    data, addr = server.recvfrom(1024)   # buffer size is 1024 bytes
    print "received message:", data

server.shutdown(socket.SHUT_RDWR)
server.close()
