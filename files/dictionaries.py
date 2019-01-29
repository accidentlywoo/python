#컬렉션(Collection)
# 리스트나  딕셔너리 같은 변수를 갖는  상황이며 하나의 정보보다는 여러 개의 정보를 저장할 때 사용된다.

#List
# 리스트는 순서대로 정리된 컬렉션이다. 데이터를 추가하면 항상 리스트의 끝에 추가되고 0부터 n-1까지 순서대로 n개의 원소가 저장

#Dictionary
# 리스트와 달리 딕셔너리에는 순서라는 것이 없다.
# 대신 키(key)라는 것이 존재.
# dict()라는 생성자를 통해 생성할 수 있다.
purse = dict() # 또는 purse = {}와 같이  생성할 수도 있다.
purse['money'] = 12 #'money'라는 키에 12라는 값 연결
purse['candy'] = 3 # 'candy'라는 키에 3이라는 값 연결
purse['tissues'] = 74 # 'tissues'라는 키에 75라는 값 연결

print(purse)
#['money':12,'candy':3,'tissues':75] 순서 보장이 안된다.

print(purse['candy']) # 3

purse['candy'] = purse['candy'] + 2 # 접근한 내용을 업데이트할 수 있다.
print(purse)
#['money':12,'candy':5,'tissues':75]

# 연관 배열(Associative Arrays)
# 키와 값이 연결되는 개념을 보통 연관 배열이라고 한다.
# 리스트에는 위치와 값 사이에 연결관계가 있다. 그러나 위치와의 연결 관계가 비교적 덜 강력하고 덜 유연
# 그래서 대부분의 현대 프로그래밍 언어에는 연관 배열이라는 개념이 있다.

# property maps : Perl / PHP
# hash maps : Java
# property bags: C# / .Net

# 이름 빈도수 세기
# 1)새로운 이름을 보면 목록에 추가한다.
# 2)추가된 이름이 1번 나왔다는 표시를 한다.
# 3)목록에 있는 이름이면 기존의 숫자에 1을 더해준다.
# 4)모든 이름을 살펴본 후 표시의 갯수를 세어 가장 높은 것을 찾는다.
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
# ['csev':1, 'cwen':1]
ccc['cwen'] = ccc['cwen'] + 1
# ['csev':1, 'cwen':2]

# 가장 중요한 부분은 이미 저장되어 있는 이름인지 확인하는 부분

#ccc = dict()
#print(ccc['csev'])

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'csev'

# IN 연산자
# 이런 문제를 for, list,문자열에서 사용했던 in연산자를 사용해 해결할 수 있다.
'csev' in ccc
# False

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name in counts:
        counts[name] = counts[name]+1
    else:
        counts[name] = 1
print(counts)

#['csev':2, 'zqian':1, 'cwen':2]

counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name] = counts[name]+1
print(counts)
#['csev':2,'zqian':1,'cwen':2]

# get메소드
# 딕셔너리에 존재하는 키인지 아닌지 여부에 따라 처리하는 패컨은 get이라는 메소드를 사용해서 간결하게 해결할 수 있다.
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0)+1
print(counts)

#['csev':2,'zqian':1,'cwen':2]
