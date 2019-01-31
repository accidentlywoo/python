#Writing programs (or programming) is a very creative and rewarding activity.  You can write programs for many reasons ranging from making your living to solving a difficult data analysis problem to having fun to helping someone else solve a problem.  This book assumes that everyone needs to know how to program and that once you know how to program, you will figure out what you want to do with your newfound skills.
# 긴 문장의 형태의 데이터를 어떻게 단어로 바꿀 수 있는지 알아보겠습니다.

#Split 메소드
#  문자열에 split메소드를 실행시키면 다음과 같이 띄어쓰기를 기준으로 문장을 분할해 단어들의 리스트로 만들어줌
# (별도의 옵션을 사용하면 공백 문자(스페이스바)가 아닌 다른 문자를 기준으로 분할할 수 있다.)
line = 'The general pattern to count the words'
print(line.split())
#['The','general','pattern','to','count','the','words']

counts = dict()
line = 'The general pattern to count the words in a line of test is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently.'
words = line.split()
print('Words:',words)
# Words: ['The', 'general', 'pattern', 'to', 'count', 'the', 'words', 'in', 'a', 'line', 'of', 'text', 'is', 'to', 'split', 'the', 'line', 'into', 'words,', 'then', 'loop', 'through', 'the', 'words', 'and', 'use', 'a', 'dictionary', 'to', 'track', 'the', 'count', 'of', 'each', 'word', 'independently.']
# ->단어로 쪼개고 싶은데 특수문자처리는 안되있넴!
for word in words:
    counts[word] = counts.get(word,0)+1
    print('Counts', counts.get(word,0))

print('Counts', counts)

# dictionary loop 적용하는 방법
counts = {'chuck':1,'fred':42,'jan':100}
for  key in counts:
    print(key, counts[key])
#check 1
#fred 42
#jan 100

jjj = {'chuck':1,'fred':42,'jan':100}
print(list(jjj))
#['jan','check','fred'] - 키로만 구성된 리스트를 얻을 수 있다.
print(jjj.keys())
#['jan','check','fred'] - 키로만 구성돤
print(jjj.values())
# [100, 1, 42]

# items 메소드의
# dictionary에 메소드를 실행하면 '튜플(tuple)'이라는 자료 구조 안에 키와 값이 쌍을 이루어 저장된 리스트가 반환된다.
jjj = {'chuck':1,'fred':42,'jan':100}
print(jjj.items())
#[('jan',100),('chuck',1),('fred',42)]
for aaa,bbb in jjj.items():
    print(aaa,bbb)
# check 1
# fred 42
# jan 100

name = input('Enter file')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

print(counts)
#  Enter file:words.txt

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
# Enter file: words.txt
# to 16

# 텍스트 파일에서 데이터를 읽어와 가장 많이 나온 단어를 출력하는 프로그램의 전체 코드는 다음과 같다.
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bogcount = count
print(bigword, bigcount)

# 실습
frame = input('Enter File:')
if len(fname) < 1:fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0)+1

largest = -1
theword = None
for k,v di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k

print('Done',theword,largest)
