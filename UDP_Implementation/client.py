import socket
udpsocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udpsocket.sendto(str.encode("Client is connected!"), ("localhost", 7777))

req = udpsocket.recvfrom(1024)
print(req[0].decode())

while(1):
    message = input("ME: ")
    udpsocket.sendto(str.encode(message),("localhost",7777))

    req = udpsocket.recvfrom(1024)
    print("Server : ", req[0].decode())




