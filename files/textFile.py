#open()
#open()함수를 이용해 파일을 열 수 있다.
#open()함수는 handle을 반환하게 되고, handle은 파일에 ㄷ ㅐ한 작업을 수행하기 위해 사용된다.
#handle은 텍스트가 파일 형태, 메모리에 저장된 문자열의 형태, 웹 사이트에서 존재하는 형태와 같이 다른 방식으로 저장되어 있는
#텍스트를 처리하는 하나의 표준화된 방식. 또한, 많은 양의 문자 파일을 한꺼번에 읽어 발생할 수 있는 성능의 문제를 hendle은 점진적으로 읽어 방지
fhand= open('hello.tx','r')
print(fhand)
#open('파일명  입력','모드 선택')
#1. 파일명 입력
# 파일명은 문자열 타입으로 입력하며, 확장자까지 포함시켜 줍니다.
#2.모드 선택
# 모드에서는 w또는 r 두가지를 선택할 수 있습니다.'w'는 파일을 작성할 때 사용하며,'r'은 파일을 읽을 때 사용
stuff1 = 'Hello World!'
print(stuff1)
print(len(stuff1))
stuff2='Hello\nWorld!'
print(stuff2)
print(len(stuff2))

fhand= open('hello.tx')
count = 0
for line in fhand:
    count = count+1
print('Line Count: ',count)
#rstrip()
#오른쪽에서 부터 공백을 지울 수 있음
# 개행 문자는 '공백'으로 취급되어 제거됨

#특정문자열이 있는 헹을 선택하기
fhand = open('hello.tx')
for line in fhand:
    line = line.rstrip()
    if not '@naver.com' in line :
        continue
    print(line)

#파일 명 입력시 NPE 피하기
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot ne opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count,'subject lines in',fname)
