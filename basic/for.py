#Definite Loops
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

friends = ['Connect','Korea','NHN']
for friend in friends:
    print('Happy New Year!!', friend)
print("Done!")

largest_so_far = -1 #값을 가지고 있는 변수를 선언해 줍니다. 작은 수로 -1을 선언합니다.
print('Before',largest_so_far)#최초의 값과 루프 이후의 값을 비교하기 위해 print함수로 현재의 값을 확인합니다.


largest_so_far = -1
print('Before', largest_so_far)
numbers = [9, 41, 12, 3, 74, 15]
for the_num in numbers : #numbers의 요소들을 다 비교하면 for문이 끝난다.
    if the_num > largest_so_far :
        largest_so_far = the_num
    print('largest_so_far: ', largest_so_far, 'current number: ',the_num)

print('After', largest_so_far)

#Counting in a Loop
zork = 0
print('Before',zork)
numbers = [9,41,12,3,74,15]
for thing in numbers:
    zork = zork +1
    print(zork,thing)
print('After',zork)

#caculate total sumary
zork = 0
print('Before', zork)
numbers = [9,41,12,3,74,15]
for thing in numbers:
    zork = zork + thing
    print(zork, thing)
print('After', zork)

#caculate total average
count = 0
sum = 0
print('Before', count, sum)
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers:
    count = count + 1
    sum = sum + value
    print(count,sum,value)
print('After',count,sum,sum/count) # After 6 154 25.666666666666668 - 소숫점 16자리

#filtering using Loop
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers:
    if value > 20:
        print('Large number', value)
print('After')

#using Boolean explores the values
found = False
print('Before',found)
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers:
    if value ==3:
        found = True
        print(found, value)
        break # 특정 값을 찾았을 떄 해당 후프를 종료하는 것이 더욱 적절해 보인다.
print('After', found)

# Minimum value explore
smallest = None
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers:
    if smallest is None:
        smallest = value
    elif  value < smallest:
        smallest = value
    print(smallest, value)
print('After',smallest)

num = 0
tot = 0.0
while True:
    sval = input('Enter a number.')
    if sval =='done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    num = num + 1
    tot = tot + fval
print(tot,num,tot/num)
