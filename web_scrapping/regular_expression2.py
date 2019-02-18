# 패턴 추출하기
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

#['2','19','42']

z = re.findall('^[AEIOU]+',x)
print(z)
#[]
z = re.findall('^[aeiou]+',x)
print(z)
#[]
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)
# ['From: Using the:']

# From:
# From: Using the:
#다음 두가지 부분이 모두 패턴과 일치하게 된다.
# 이럴 때는 다음과 같이 가장 긴 패턴을 찾아주는데, 이것을  '탐욕적 방식의 패턴 찾기'라고 부릅니다.

y = re.findall('^F.+?:',x)
print(y)
#['From:']

# 비 탐욕적 방식의 패턴 찾기
# 다음 코드 처럼 패턴뒤에 '?'를 붙여주면 여러 대상 중 가장 짧은 것을 선택하게 된다.

#원하는 부분만 추출하기
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('\S+@\S+',x)
print(y)
# ['stephen.marquard@uct.ac.za’]
# '@'문자 앞 뒤로 공백이 아닌 문자가 오는 문자열 패턴을 찾아줍니다.

y = re.findall('^From (\S+@\S+)',x)
print(y)

# ['stephen.marquard@uct.ac.za']
# '()'사용헤서, From으로 시작하느 이메일 주소 패턴에서 이메일 주소 부분만 추출할 수도 있다.

#이메일 호스트를 추출하는 다양한 바업ㅂ
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
# 21
sppos = data.find(' ',atpos)
print(sppos)
# 31
host = data[atpos+1 : sppos]
print(host)
# uct.ac.za

# find 메소드와 리스트 슬라이싱을 활용해 다음과 같이 찾을 수 있었습니다.

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
# 'uct.ac.za'

# 정규식을 활용
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)

# 종합예제 : 패턴 추출 및 최댓값 찾기
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-ConfidenceL([0-9.]+)',line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

#예외 문자(Excape Character)
x = 'We just recieved $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)
#['$10.00']
