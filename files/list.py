a=[1,2,3]
b=[4,5,6]
c = a+b
print(c)
#[1,2,3,4,5,6]로 출력됩니다.

#list Slicing
t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#dir() 메소드
# 특정 타입에서 사용할 수 있는 메소드의 목록들을 볼 수 있는 함수도 있습니다.
x = list()
print(dir(x))

#리스트 만들기
#빈 리스트 만들기 - 항목 추가하기 - 항목정렬하기 - in을 활용해 'Glenn'이 친구 목록에 있는지 확인하기
friends = list()
friends.append('Joseph')
friends.append('Glenn')
friends.append('Sally')
print(friends)
#['Joseph','Glenn','Sally']
friends.sort()
print(friends)
#['Glenn','Joseph','Sally']
print('Glenn' in friends)
#True로 출력된다.

abc = 'With three words'
stuff = abc.split()
print(stuff)
#['With','three','words']로 출력됩니다.

#구분자
#명시적으로 구분자를 넣어주지 않으면, 빈칸을 구분자로 인지하고 나누게 됩니다.
words = 'first;second;third'
stuff2 = words2.split()
print(stuff2)
#['first;second;third']
stuff2 = words2.split(';')
print(stuff2)
#['first','second','third']

#이메일 주소 추출하기
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#line 에 uct.ac.za만 추출하는 방법을 찾아 보도록 하겠습니다.
words = line.split()
#words는 해당 라인을 빈칸을 구분자로 하여 리스트로 저장됩니다.
print(words[1])
#stephen.marquard@uct.ac.za이 출력됩니다.
email = words[1]
address = email.split('@')
pront(address)
#['stephen.marquard','uct.ac.za'] 가 출력됩니다.
print(address[1])
#uct.ac.za가 출력됩니다.

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()

    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
