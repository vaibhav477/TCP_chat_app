import socket
udpsocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpsocket.bind(("localhost",7777))
print("UDP server is up and listening")

pair = udpsocket.recvfrom(1024)
res = pair[0]
add = pair[1]
print("Response from client :")
print("Message Received: ", res.decode())

print("Address of client: ", add, end = '\n\n')

udpsocket.sendto(str.encode("Connected to Server!"), add)

while(True):
    pair = udpsocket.recvfrom(1024)
    res = pair[0]
    add = pair[1]
    print("Client: ", res.decode())

    message = input("ME: ")
    udpsocket.sendto(str.encode(message), add)




