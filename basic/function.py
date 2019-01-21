def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()
# 함수를 정의할 떄 def예약어 사용.
def greeting():
    print("Hello World")

greeting()

def greet():
    return "Hello"

print(greeting(),"Connect")
print(greeting(),"Python")

def add(left, right):
    return left + right

print(add(1,2));

def computepay(hours,rate):
    if hours > 40:
        reg = rate*hours
        otp = (hours-40.0)*(rate*0.5)
        pay = reg +  otp
    else:
        pay = hours*rate
    return pay

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay",xp)
