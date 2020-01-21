# 클래스 기본 
# 클래스 : 함수 + 변수 모아 놓은 것
# 오브젝트(object) == 인스턴스(instance) : 클래스를 이용해 만들어낸 물체(클래스 써서 만든것)
# 클래스 기본구조

## 클래스 기본구조 
class Person:
    name = "윤상현"

    #self : 만들어진 클래스의 변수를 활용 해야할때 사용
    def say_hello(self):
        print("안녕! 나는 " + self.name)

p = Person()
p.say_hello()

















