# 클래스 상속
# 공통 클래스가 하나있고 조금 다른 세부 클래스를 만들고 싶을때 사용
# 상속 (inheritance)


## 상속 (inheritance)
# 예를 들어 결찰 클래스, 프로그래머 클래스가 있다면 
# 경찰 클래스 와 프로그래머 클래스 끼리 할수 있는 것은 달라야하며
# Person 클래스에서 할수 있는 것은 두 클래스가 다 할수 있어야 한다.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 "+ self.name)
    
    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

#Police(Person) : Police란 클래스가 Person이란 클래스를 상속
class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다. " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야겠다 : " + to_program)

wonie = Person("워니", 20)
jenney = Police("제니", 21)
michael = Programmer("마이클", 22)

jenney.introduce()
jenney.arrest("워니")
michael.introduce()
michael.program("이메일 클라이언트")