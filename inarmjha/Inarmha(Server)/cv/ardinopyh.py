import socket

s=socket.socket()
host=""
port=1934

s.connect((host,port))
s.send("hi")
s.close
