n = 5
while n>0:
    print(n)
    n=n-1
print('Blastoff')
print(n)

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('DONE~')
#무한으로 돌 수 있다
# -> 코드가 복잡해질 수록 반복문이 종료될 수 있다는 것을 확신할 수 없다.
