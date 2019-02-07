# List vs Tuple
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1,9,2)
print(y)
print(max(y))

for iter in y :
    print(iter)
# Immutable
# Tuple 과 List의 큰 차이점은 Tuple은 변경불가능 하다는 것
x = [9,8,7]
x[2] = 6
print(x)
#[9,8,6]

xx = (9,8,7)
xx[2] = 6
print(xx)
#error
# 이런 변경 불가능한 속성 때문에 튜플은 리스트보다 더 효율작으로 동작.
# 용량도 적게 차, 접근도 뤌씬 빠르다.

i  = list()
dir(i)
#['append','count','extend','index','insert','pop','remove','reverse','sort']

t = tuple()
dir(t)
#['count','index']

#튜플의 장점
# 임시 변수로 활용 - 좌변과 우변의 갯수는 일치해야한다.
(x,y) = (4,'fred')
print(y)
#fred
(a,b)  = (99,98)
print(a)
#99

def t():
    return (10,20)
x,y  = t()
print(x,y)
#10 20

x,y = 1,10
print(x,y)
# 1 10

x,y = y,x
print(x,y)
# 10 1

#딕셔너리를 처리하는데 활용
d =  dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)
# csev 2
# cwen 4

tups = d.items()
print(tups)
#dict_items([('csev',2),('cwen',4)])

#여러 값에 대해 비교가능
(0,1,2) < (5,1,2)
#True
(0,1,20000000) < (0,3,4)
('Jones','Sally') < ('Jones','Sam')
#True
('Jones','Sally') < ('Adams','Sam')
#True

# 키를 기준으로 정렬하기
# 1. 딕셔너리에서 items 메소드를 실행해 튜플로 이루어진 리스트 형태로 만든다.
# 2. 이 리스트를 sorted 함수로 정렬한다.
d  = {'b':1, 'a':10,  'c':22}
d.items()
#dict_items([('b',1),('a',10),('c',22)])
sorted(d.items())
# [('a', 10), ('b', 1), ('c', 22)]

for k,v in sorted(d.items()):
    print(k,v)
# a 10
# b 1
# c 22

#값을 기준으로 항목정렬하기
# 1. 딕셔너리에서 items 메소드를 실행한다.
# 2. 튜플을 활용해 키와  값을 분리한다.
# 3. 키와 값의 위치를 바꾼 리스트를 생성한다.
# 4. 생성된 리스트를 정렬한다.
c={'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))

print(tmp)
#[(10,'a'),(1,'b'),(22,'c')]
tmp = sorted(tmp)
print(tmp)
#[(1,'b'),(10,'a'),(22,'c')]

c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))

print(tmp)
#[(10,'a'),(1,'b'),(22,'c')]
tmp = sorted(tmp,reverse = True)
print(tmp)
#[(22,'c'),(10,'a'),(1,'b')]

#가장 많이 등장한 단어 Top 10
fhand = open('romeo.txt')
counts = {}
for line  in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst = []
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val,key in lst[:10]:
    print(key,val)

fhand = open('romeo.txt')
counts = 0
for line in  fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst = []
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse = True)

for val,key in lst[:10]:
    print(key,val)

# 리스트 컴프리헨션(List Comprehension)
c ={'a':10,'b':1,'c':22}
tmp = list()
for k, v in c.items():
    tmp.append((v,k))

tmp = sorted(tmp)
print(tmp)

#[(1,'b'),(10,'a'),(22,'c')]

#실습
fname = input('Enter File:')
if len(fname) < 1:fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds :
        di[w] = di.get(w,0)+1

tmep = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp,reverse = True)

for v,k in tmp[:5]:
    print(k,v)
