# TCP(전송 제어 프로토콜)
# Transport 계층 - Transport 계층 (Peer to Peer)
# IP(인터넷 프로토콜)위에서 구성, IP는 데이터를 잃어버릴 수 있음.데이터를 저장하고 있다가 손실이 일어난 것으로 추정되면 재전송
# 전송 윈도우를 통해 흐름 제어를 조절
# 믿을만한 pipe 역할을 제공

# TCP 연결 / 소켓
# 컴퓨터 네트워킹에서 인터넷 소켓, 또는 네트워크 소켓은 인터넷 프로토콜을 기반으로 한 인터넷 등의 컴퓨터 네트워킹에서 양방향
# 커뮤니케이션의 끝점입니다. 프로세스 <- 인터넷 -> 프로세스

# TCP 포트번호
# 포트는 애플리케이션에 대응되거나 프로세스에 대응되는 소프트웨어 커뮤니케이션의 말단
# 한 서버에 여러 네트워크 애플리케이션이 존재할 수 있게 해줌

# 공통 TCP 포트
# - Telnet (23) : Login      - IMAP (143/220/993) : Mail
# - SSH (22) : Secure Login  - POP (109/110) : Mail Retrieval
# - HTTP (80)                - HTTPS (443) : Secure
# - DNS (53) : Domain Name   - SMTP (25) : Mail
# - FTP (21) : File Transfer

# 파이선 내부적으로 TCP 소켓을 지원
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# 'data.pr4e.org' - 호스트     80 - 포트


#애플리케이션 프로토콜
# Application 계층 - Application 계층 (Peer to Peer)
# TCP는 믿을만한 소켓을 제공. 소켓으로 어떤 일을 할 수 있고 어떤 문제를 해결?
# 애플리케이션 프로토콜 - 메일  - 월드 와이드 웹(WWW)

# HTTP(Hyper Text Transfer Protocol) - 하이퍼텍스트 전송 프로토콜
# 인터넷, 애플리케이션 레이어에서 가장 많이 사용되는 프로토콜
# 웹을 위해 개발 - HTML, Image, Documents 등을 가져옴
# 문서 외에 다양한 데이터에도 확장하여 사용 가능
#   - RSS, 웹 서비스 등
#   - 기본 컨셉 : 연결 - 문서 요청 - 문서 수신 - 연결 종료
# 브라우저가 서버로부터 인터넷을 통해 웹 문서를 받는 경우의 규칙을 정한 것

# Protocol
# 규칙의 모음. 모두가 따르므로 서로가 서로의 행동을 예측 가능
# 서로 충돌하지 않아야 함.
#   - 미국의  이차선 도로에서는 오른쪽 도로로 달려야 함
#   - 영국의 이차선 도로에서는 왼쪽 도로로 달려야 함.

# 서버로부터 데이터 받기
#   사용자가 'href=값'을 가지고 있는 앵커 태그를 클릭해 새로운 페이지로 이동할 때마다 브라우저는 웹서버와 연결을
#   먼들고 GET요청을 실행해 페이지 URL에 나타난 값을 수신
#   서버는 문서를 포맷팅하고 유저에게 보여주는 HTML문서를 리턴

# 인터넷 표준
#   모든 인터넷 프로토콜 기준은 한 기관에 의해 개발
#   Internet Engineering Task Force(IETF)
#   www.ietf.org
#   기준은 "RFCs"라고 부름 - "Request for Comments"

# Python 에서의 HTTP 요청
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STRAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode(),end='')
mysock.close()

# 문자와 문자열에 대해
#   ASCII(American Standard Code for Information Interchange)

# 간단한 문자열 표현방법
# 각 문자는 0~256 사이의 숫자로 대응되어 저장되며, 이는 메모리에서 8비트를 차지
# 8비트를 메모리에서 "byte"로 정함(예:"내 USB는 8기가 바이트짜리야")
# ord() ASCII 문자에 대응되는 숫자를 리턴

# 여러 바이트로 된 문자
#   UTF-16 : 길이 고정됨 2바이트
#   UTF-32 : 길이 고정됨 4바이트
#   UTF-8 : 1-4 bytes
#     - ASCII를 포함하며, 호환
#     - ASCII를 자동으로 감지 가능
#     - UTF-8은 시스템 간에 데이터를 교환할 때 가장 실용적으로 추천되는 인코딩 형식입니다.

# Python 2.7.10
x = '이광춘'
type(x)
#[type 'str']

x = u'이광춘'
type(x)
#[type 'unicode']

#Python 3.5.1
x = '이광춘'
type(x)
#[class 'str']

x = u'이광춘'
type(x)
#[class 'str']

# 파이썬 3에서 모든 문자열은 유니코드임
#  -> 파일에서 데이터를 가져와 파이썬에서 작업하는 경우 거의 대부분 "그냥 작동"합니다.
#  그러나 소켓을 통해 네트워크로 데이터를 전송하거나 DB와 연결하는 경우 데이터를 인코딩/디코딩해야 함(UTF-8이 많이쓰임)

#파이썬 문자열에서 Byte로
#   네트워크 소켓 등 외부 자원과 통신하는 경우, 문자열이 아니라 Byte 형식을 사용해야함.
#   따라서 파이썬 3에서는 문자열을 Byte로 인코딩 필요.
#   외부에서 데이터를 가져오는 경우 해당 문자셋에 대하여 디코딩을 해야 파이썬3에서 정상적인 문자열으로 사용할 수 있다.
