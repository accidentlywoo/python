# 웹 상의 데이터
# -HTTP 요청과 응답에 대한 이해와 지원을 바탄으로, 이 프로토콜을 이용한 프로그램간의 정보 교환릐 추세
# -네트워트와 응용프로그램 간의 데이터 표현 방식에 있어서 합의가 필요.
# - 네트워크를 통한 정보 전송
#       {                           <-> php 배열
#       "name":"Chuck",             <-> 파이썬 딕셔너리
#       "phone":"303-4456"          <-> 자바스크립트 객체
#       }                           <-> 자바 HashMap
# a.k.a '와이어 프로토콜' - 우리가 '와이어'상에 보내는 것

# XML(eXtensible Markup Language)
# 정보 시스템이 구조화된 데이터를 공유하는 것이 초기 목적
# 표준 범용 교정 용어 (SGML)의 간소화된 버전으로 시작하였고, 조금더 인간에게 친숙한 방향으로 디자인

# '와이어 포맷' 합의하기

#   파이썬 딕셔너리 -직렬화->
# <person><name>Chuck</name></person>       (XML)
#   -역 직랼화-> 자바 HashMap

#   파이썬 딕셔너리 -직렬화->
#{"name":"Chuck"}                           (JSON)
#   -역 직렬화-> 자바 HashMap

#XML 요소들(또는 노드)

#   단순 요소 : <name>Chuck</name>
#   복합 요소 : <person><name>Chuck</name></person>

# XML의 기초

# 시작 태그 : <person>, < name>
# 끝 태그 : </person>, </name>
# 문자정보 text element : Chuck
# 속성 attrivutes : <phone type="init">
# 스스로 닫는 태그 self closing tag : <email />

# 공백  : 줄의 끝은 중요하지 않음. 문자 요소에서 공백은 없어짐. 오직 가독성만을 위해 들여쓰기를 함.

# 직렬화 Serialize/ 역직렬화 De-Serialize
#       : 한 프로그램의 데이터를 특정 프로그램 언어에 제한되지 않은 채로 시스템 내에 저장되고 전달되어질 수 있는
#        형식으로 변환하는 것.

# XML 스키마
#   : XML이 받아들이는 형태의 "약속"을 설명
#   : XML 문서의 올바른 형식에 대한 설명
#   : 문서의 구조와 내용에 대한 제한의 형식으로 표현됨.
#   : 시스템 간의 "약속"을 표현할 때 주로 사용됨 - "내 시스템은 이 스키마에 맞는 XML만 수용할 거야"
#   : 특정 XML이 스키마의 사항들을 만족할 때 우리는 그것은 "타당하다(validate)"라고 한다.

# XML 문서 : <person><lastname>Severance</lastname></person>    ->
# XML 스키마 계약서 : <xs:complexType name="person"><xs:sequence><xs:element name="lastname" type="xs:string"/></xs:sequenve></xs:complexType>

# 여러 XML 스키마 언어
#문서타비 정의 Document Tyep Definition(DTD)
#표쥰 범용 교정용어 (ISO 8879:1986 SGML)
#XML 스키마 W3C (XSD)

# XSD XML  스키마 (W3C spec)
#   우리는 World Wide Web Consortium(W3c)버전에 집중할 것
#   따로 "W3C스키마"라고 불리는 이유는 "스키마"가 포괄적인 표현이기 때문
#   흔히 XSD라 불리는 이유는 파일 확장명이 .xsd이기 때문
