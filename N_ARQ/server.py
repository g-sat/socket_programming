import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(), 12345))
soc.listen(5)

while True:
    clientsocket, address = soc.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))