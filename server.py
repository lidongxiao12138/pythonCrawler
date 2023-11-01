#server.py

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost' #L'IP du Serveur
port = 1234 #data transfering port

server.bind((host,port)) #bind server
server.listen(5)

client, addr = server.accept()
print("Got Connection from",addr)

client.send("李东晓接受到了消息 :)".encode('UTF-8')) #send data to client
msg = client.recv(1024)
print(msg.decode('UTF-8'))
input()