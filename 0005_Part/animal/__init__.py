# 이 폴더가 패키지 라고 말을 하고 싶으면 __init__.py 파일 만들어야함
# 이 폴더가 어떤 모듈의 합이라고 설정을 해야함
# 그래야 사용가능
from .cat import Cat # . <- 이 폴더에 있는 cat.py 이라는 파일에서 Cat 이라는 클래스를 갖고와줘
from .dog import Dog # . <- 이 폴더에 있는 dog.py 이라는 파일에서 Dog 이라는 클래스를 갖고와줘