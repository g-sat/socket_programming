import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((socket.gethostname(), 12345))

msg = soc.recv(1024)
print(msg.decode("utf-8"))