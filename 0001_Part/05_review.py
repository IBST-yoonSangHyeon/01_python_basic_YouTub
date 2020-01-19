# 인사를 하는 함수 만들어보자
# 함수 역할
# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕" 이라고 말해라
# 나이가 10살에서 20살 사이이면 "안녕하세요" 라고 말해라
# 그 외에는 "안녕하십니까" 라고 말해라

def sayHello(name, age):
    if age < 10:
        print("안녕, "+ name)
    elif age <= 20 and age >= 10:
        print("안녕하세요, " + name)
    else:
        print("안녕하십니까, " + name)

sayHello("윤상현", 9)
sayHello("윤상현1", 20)
sayHello("윤상현2", 40)
