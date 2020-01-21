# 클래스 init
# __inti__ 함수

## __inti__ 함수
#nme 변수를 "윤상현"으로 고정시키지 않고 오브젝트를 만들때 새로 이름을 짓고 싶을때
class Person:

    #__init__ 초기화(initialization) 함수
    def __init__(self, name, age):
        self.name = name
        self.age = age

        

    #self : 만들어진 클래스의 변수를 활용 해야할때 사용
    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 "+ self.name)
    
    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

yoonsh = Person("윤상현",30)
yoonsh.say_hello("수영")
yoonsh.introduce()