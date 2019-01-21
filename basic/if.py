x=5;
if x<10:
    print('Smaller')
if x>20:
    print('Bigger')

print('Finis')

if x<2:
    print('Below 2')
elif x>=2:
    print('Two or more')
else:
    print('Something else')
# Indentation
# Maintain indent scope
astr="123"

try:
    print("Hello")
    isInt = int(astr)
    print("World")
except:
    isInt = "Integer로 변경할 수 없습니다."

print('Dont',isInt)

sh = input("Enter Hours : ")
sr = input("Enter Rate : ")
fh =  float(sh)
fr = float(sr)
#print(fh,fr)
if fh > 40:
    #print("Overtime")
    reg = fr*fh
    otp = (fh - 40.0)*(fr*0.5)
    #print(reg,otp)
    xp = reg+otp
else:
        #print("regular")
        xp = fh*fr
print("Pay:",xp)
