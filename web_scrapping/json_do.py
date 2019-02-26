#JSON(JavaScript Object Notation)
#   XML보다 더 자주 사용되는 데이터 포멧. 이 코드는 이전 시간에 XML로 실행했던 것과 정확히 같은 내용의 코드
#   데이터가 XML형식에서 JSON 형식으로 바뀐 것을 제외하면 말입니다.
# JSON은 파이썬에서 딕셔너리와 굉장히 비슷하기 때문에 데이터를 읽어온 후 딕셔너리로 접근할 수 있다.
import JSON
data = '''{
    "name":"Chuck",
    "phone":{
        "type":'intl',
        "number":"+1 734 303 4456"
        },
    "email":{
            "hide":"yes"
        }
}'''
info  = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

# Name : Chuck
# Hide : yes

#여러개의 데이터를 읽어올 경우  리스트에 딕셔너리가 포함된 형태로 읽어집니다.
import json
input = '''[
    {
    "id":"001",
    "x":"2",
    "name":"Chuck"
    },
    {
    "id":"009",
    "x":"7",
    "name":"Chuck"
    }
]'''

info = json.loads(input)
print(info)
print('User count',len(info))
for item in info:
    print('Name',item['name'])
    print('Id',item['id'])
    print('Attribute',item['x'])

# [{'id':'001','x':'2','name':'Chuck'},{'id':'009','x':'7','name':'Chuck'}]
# User count: 2
# Name count:2
# Name Chuck
# Id 001
# Attribute 2
# Name Chuck
# Id 009
# Attribute 7
