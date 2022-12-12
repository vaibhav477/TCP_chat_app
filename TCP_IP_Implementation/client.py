import socket
tcpsocket = socket.socket()
name = input("Enter your name : ")
port = 7777
tcpsocket.connect(('localhost', port))
print("Connected to the server...\n")

tcpsocket.send(name.encode())
server_name = tcpsocket.recv(1024).decode()
print(server_name, "has joined the chat")
print("Type exit to leave the chat")

while True:
    message = tcpsocket.recv(1024)
    message = message.decode()
    print(server_name, ":", message)
    message = input(str("Me : "))
    if message == "exit":
        message = "Left"
        tcpsocket.send(message.encode())
        tcpsocket.close()
        break
    tcpsocket.send(message.encode())




