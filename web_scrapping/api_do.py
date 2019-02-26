# API(Application Program Interface)
#   API는 인터페이스를 지정하고 그 인터페이스의 객체의 행동을 제어한다는 점에서 매우 추상적.
#   API에 명시된 기능을 제공하는 소프트웨어를 API의 "실행"이라고 하며,
#   API는 대체로 애플리케이션을 구성하게 되는 언어로 정의됨.

# API를 실행하기 위한 계산 자원은 "무료"가 아님
# API를 통해 제공된 데이터는 대체로 매우 가치가 높음
# 데이터의 제공자는 하루 요청량을 제한하여서 API의 "키"를 요구하거나, 사용료를 부과하기도 함
# 발전을 거치면서 여러 규칙들이 바뀌기도

# ㅡㅡㅡㅡㅡ 정리 ㅡㅡㅡㅡㅡ
# 서비스 지향 아키텍쳐 - 애플리케이션이 부분적으로 나위어 네트워크 상에 퍼질 수 있게함
# 응용 프로그램 인터페이스(API) 상호 작용에 대한 계약/약속
# 웹서비스는 애플리케이션끼리 네트워크 상에서  현력할 기반을 제공함 - SOAP와 REST는 웹서비스의 두 가지 형태
# XML과 JSON은 직렬화 형식
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location:')
    if  len(address) < 1:break

    url = serviceurl + urllib.parse.urlencode({'address':address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location  = js['results'][0]['formatted_address']
    print(location)

    # Enter location : Korea, Seoul
    # Retrieving http://maps.googleapis.com/maps/api/geocode/json?address=Korea%2C+Seoul
    # Retrieved 1517 characters
    # lat 37.566535 lng 126.9779692
    #Seoul, South Korea
    
