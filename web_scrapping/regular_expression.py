#^           라인의 처음을 매칭
#$            라인의 끝을 매칭
#.             임의의 문자를 매칭 (와일드 카드)
#\s          공백 문자를 매칭
#\S         공백이 아닌 문자를 매칭
#*            바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 표기함.
#*?          바로 앞선 문자에 적용되고 0 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
#+           바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 표기함
#+?          바로 앞선 문자에 적용되고 1 혹은 그 이상의 앞선 문자와 매칭을 탐욕적이지 않은 방식으로 표기함.
#[aeiou]    명세된 집합 문자에 존재하는 단일 문자와 매칭. “a”, “e”, “i”, “o”, “u” 문자만 매칭되는 예제
#[a-z0-9]    - 기호로 문자 범위를 명세할 수 있다. 소문자이거나 숫자인 단일 문자만 매칭되는 예제.
#( )         괄호가 정규표현식에 추가될 때, 매칭을 무시한다. 하지만 findall()을 사용 할 때 전체 문자열보다 매칭된 문자열의 상세한 부속 문자열을 추출할 수 있게 한다.
import re
# re(regular expression)모듈을 import해야 정규표현식을 사용할 수 있다.

hand = open('https://www.py4e.com/code3/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

#같은 프로그램을 정규식을 활용하여 작성하면 다음과 같습니다.

hand = open('https://www.py4e.com/code3/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:',line):
        print(line)

#텍스트에서 시작 패턴 찾기
# 'From:'으로 시작하는 문장을 출력하는 프로그램입니다.
hand = open('https://www.py4e.com/code3/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

hand = open('https://www.py4e.com/code3/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)
