# 패키지 
# 패키지(package) == 라이브러리(library): 어떤 기능의 모듈들의 합
# 패키지 == 모듈1 + 모듈2 + ...
# 모듈 == 코드 들어있는 파일 : 이 코드가 모여서 어떤 한 기능을 구현함
# 패키지 만들기
# 패키지 사용하기

# 패키지가 굳이 왜 있을까?
# 예를 들어 날씨 서비스를 A 프로그래머가 개발을 했다면
# 다른 서비스에서 해당 서비스를 구현을 따로 할 필요 없이 
# A 프로그래머가 날씨 서비스를 패키지화 하여 
# 공유를 하면 다른 서비스에서 활용하도록 하는것 
# 그런데 프로그래머가 자선사업가는 아니다.... 그럼 또 패키지 굳이 왜할까?
# A 회사에서 B1 프로젝트 개발도중 A1 이라는 서비스를 만들게 되었는데
# B2 프로젝트를 개발 당시 B1 프로젝트에 쓰인 A1 서비스가 필요한 상황이 생겼을경우
# A1 서비스를 패키지화 하여 B2 프로젝트에 따로 구현 필요없이 사용되도록 하면 
# 시간 절약으로 인해 비용 절감이 될것이다.

## 패키지 만들기
# 패키지 만들기 목표
# animal package(폴더 이름)
# dog, cat modules
# dog, cat modules can say "hi"

## 패키지 사용하기
from animal import dog # animal 패키지 에서 dog 라는 모듈을 갖고 와줘
from animal import cat # animal 패키지 에서 cat 라는 모듈을 갖고 와줘

# from animal.dog (animal 패키지에서 dog이란 모듈을 불어와서) import Dog (Dog이란 클래스 가져와줘)

from animal import * # animal 패키지 에서 갖고 있는 모듈을 다 불러와

# * 아닌 것으로 import 한거로 사용함
d = dog.Dog() # instance
d.hi()

c = cat.Cat()
c.hi()

# * import 한거로 사용함
a = Dog()
b = Cat()
a.hi()
b.hi()




