import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))

# XML Schema
# XML 데이터를 파이썬에 읽어오기 위해서는 xml 모듈이 필요합니다.
# 다음돠 같은 함수를 활용하면 XML에 접근해 원하는 데이터를 추출할 수 있습니다.
import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))

# Name:Chuck
# Attr:yes

# 조금 더 복잡하지만 XML의 구조를 이해하고 있으면 다음과 같이 반복문을 활용해 XML 데이터의 접근할  수도  있습니다.
import xml.etree.ElementTree as ET
input =
'''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name',item.find('name').text)
    print('Id',item.find('id').text)
    print('Attribute', item.get("x"))

#User count:2
#Name Chuck
#Id 001
#Attribute 2
#Name Brent
#Id 009
#Attribute 7
