#detail String
# 문자열 타입과 관련하여서는 타입 변환, 인덱싱, len 함수, for 루프 활용을 이해
name = input('Enter : ')
print(type(name))
print(name)
#문자열을 사용해 데이터를 읽어 오게 되면 우리는 에러나 사용자 입력에 대해 많은 대처를 할 수 있게된다.
#사용자 입력으로 들어오는 값은 문자열 타입으로 입력된다.

#뮨자열을 개별 문자 값에 인덱스를 활용해서 접근할 수 있다.
fruit = 'banana'
letter = fruit[0]
print(letter)
letter = fruit[1]
print(letter)
letter = fruit[2]
print(letter)
print(len(fruit))

index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for letter in fruit:
    print(letter)

#Slicing Strings
s = 'Monty Python'
print(s[0:4])
 #Strings start point/end point can deletion
print(s[:2])
print(s[8:])
print(s[:]) # 전체 출력

# 문자열 합치기
firstString = 'Hello'
secondString = 'There'
print(firstString+secondString)
# HelloThere로 출력된다.
thirdString = firstString+ ' '+secondString
print(thirdString)
# Hello There로 출력된다

# IN function use in Strings
fruit = 'banana'
print('n' in fruit) #True
print('m' in fruit) #False
print('nan' in fruit) #True
if 'a' in fruit:
    print('Found it!!') # Found it

# 문자열 라이브러리
greet = 'Hello Bob'
zap = greet.lower()
print(zap) # hrllo Bob
print(greet) #Hello Bob
# 참조하는 값을 변경하지 않는다.
print('Hi There'.lower()) #hi there
print(greet.upper()) #HELLO BOB

#Strip 메소드
    #문자열에서 공백을 제거할 수 있는 메소드가 존재한다.
    #lstrip() : 왼쪽 공백 제거
    #rstrip() : 오른쪽 공백제거
    #strip() : 양쪽 공백 제거
greet = '            Hello Bob     '
greet.lstrip() #Hello Bob     ;
greet.rstrip() #            Hello Bob;
greet.strip() #Hello Bob

str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
piece = str[ipos+2:]
value=float(piece)
print(value)
print(float(.1111)) #0.1111

# find() 문자열 탐색
# replace() 문자열 탐색-대체 문자열로 치환
greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr) # Hello Jane
print(greet)# Hello Bob - 원본 데이터는 변질되지 않는다.
# startswidth() 접두사
line = 'Please have a nice day'
print(line.startswith('Please')) # True
print(line.startswith('p')) # False 대소문자 구분
print(line.startswith('P')) # True
