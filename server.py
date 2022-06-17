import socket

host = ''
port = 4444

s = socket.socket()
s.bind((host,port))
s.listen(1)

conn,address = s.accept()
x = ""

while True :
    x = str(input(x))
    conn.send(str.encode(x))
    x = conn.recv(900000).decode('utf-8')

conn.close()
