import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STRAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)

# 간단한 웹 브라우저 만들기
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STRAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysocket.recv(512)
    if(len(data)<1):
        break
    print(data.decode(),end='')
mysock.close()
