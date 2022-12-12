import socket
tcpsocket = socket.socket()
port = 7777
tcpsocket.bind(('localhost', port))
name = input(str("Enter your name: "))
           
tcpsocket.listen(1)
print("Server is up and listening at port: ", port)
connection, clientaddress = tcpsocket.accept()
print("Type exit to leave the chat")
print("Received connection from the client named ",end="")

client_name = connection.recv(1024).decode()
print(client_name, "has connected to the chat")
print("Address of client", clientaddress)
connection.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "exit":
        message = "Left"
        connection.send(message.encode())
        tcpsocket.close()
        break
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    print(client_name, ":", message)




