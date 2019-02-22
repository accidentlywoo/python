# ASCII
#   아스키 코드는 1byte로 영문자와 숫자, 그리고 일부 특수문자들을 표현할 수 있습니다.
#   ord() 함수를 사용하면 다음과 같이 각각의 문자에 대한 아스키 코드 값을  확인할 수 있다.
print(ord('H'))
#72
print(ord('e'))
#101
print(ord('\n'))
#10

# Unicode
#   유니코드를 압축하는 UTF-8, UTF-16, UTF-32등 다양한 방법이 있지만 가장 실용적인 UTF-8을 사용하는 것
#   파이썬 2.x버전에서는 유니코드로 나타내고 싶으면 별도의 문자열 앞에 'u'이라는 문자를 넣어주어야 했다.

#  Python 2.7.10
x = '이광춘'
print(type(x))
#<type 'str'>
x = u'이광춘'
print(type(x))
#<type 'unicode'>

# Python 3.x 버전부터는 기본적으로 문자열이 유니코드로 저장된다.

# Python 3.5.1
x = '이광춘'
print(type(x))
#<class 'str'>
x = u'이광춘'
print(type(x))
#<class 'str'>

# 파이썬 내부에서 데이터를 사용하는 것이 아니라 네트워크를 통해 데이터를 주고 받을 때는 다른 형태로 데이터를 변환해야하는 경우도 있습니다.
#  'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n' 문자열은 유니코드입니다.
# 따라서 UTF-8 byte 방식으로 인코딩을 해주어야 하는데, 그럴 때 사용되는 메소드가 encode()입니다.
'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# 인코딩된 문자열을 소켓을 통해 전송합니다.
import socket

mysock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock2.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock2.send(cmd)

#이제 서버에서 받은 데이터를 data라는 변수에 저장합니다. 그리고 이 데이터는 현재 디코딩이 안 되어있기 때문에 decode()메소드를 사용하여
#디코딩하여 출력하면 유니코드 형태로 우리에게 보여지는 것입니다.
while True:
    data = mysock2.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock2.close()
