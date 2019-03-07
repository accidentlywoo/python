# 핵심 키워드
#   - Class     - Object    - dir()     -type()

# Class와 Object
#   다음은 PartyAnimal 클래스. 여기에서 an 이라는 객체를 만들어서 party 메소드를 3번 실행시키면 다음과 같은 결과가 출력된다.
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

# dir()과 type()
#   dir 함수와 type 함수를 사용하면 객체를 검사할 수 있다.
#   x라는 리스트를 만든 후 dir(x)라고 실행하면 다음과 같은 결과를 확인할 수 있다.
x = list()
dir(x)
'''
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__reversed__',
 '__rmul__',
 '__setattr__',
 '__setitem__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']
'''
# 여기에서 '__'로 시작해서 '__'로 끝나는 것들에 대한 설명은 생략하겠지만 그 아래에 있는 것들은 그동안 우리가 사용해왔던 메소드들이다.
# x는 리스트 객체이기 때문에. append, sort 등의 메소드를 실행시킬 수 있다는 것을 알 수 있다.
print(type(x))

#<class 'list'>
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

print("Type", type(an))
print("Dir", dir(an))
