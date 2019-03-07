# 파이썬 객체의 생명주기
#   - 객체 생명주기(Object Lifecycle)
#   - 생성자(Constructor)
#   - 소멸자(Destructor)

# Constructor와 Destructor
#   파이썬의 생성자는 __init__, 소멸자는 __del__로 정의.
#  객체를 생설할 때 생성자가 실행이 되고, 객체가 사라질 때 소멸자가 실행되는 것을 볼 수 있다.
class PartyAnimal:
    x = 0

    def __init__(self):
        print("i am Constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("i am desctructed", self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self,z):
        self.name = z
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()
# 이 코드의 결과를 보면 객체를 두 번 생성할 경우 name이라는 속성과 x라는 속성은 각각 별개의
# 값을 저장한다는 걸 알 수 있다.
