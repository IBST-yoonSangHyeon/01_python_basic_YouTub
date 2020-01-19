# 자료구조(Structure)의 튜플(Tuple) 구조
# 튜플과 리스트는 엄청 비슷함
# 튜플 기본
# 리스트는 되지만 튜플에서 안되는것  
# 가변과 불변 의미

## 튜플 기본
x = tuple()
y = ()

print(x)
print(y)

# 튜플에서도 리스트에 있는 기본적인 함수를 사용가능함
x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

print(x)
print(y)
print(z)

# 튜플도 리스트 처럼 가능한것들
print(x + y) # 리스트 합치기 가능
print('a' in y) # 리스트에서 엘리멘트 있는지 체크 가능
print(z.index(1)) # 리스트에서 엘리멘트 위치 찾기 가능


## 리스트는 되지만 튜플에서 안되는것 
# Assignment = 튜플 안의 값을 업데이트 하는 것 : Assignment 안됨
x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

# x[0] = 10 # Error !!! : 튜플은 안의 값을 한번에 바꾸지 못하는 에러 뜸

## 가변과 불변 의미
# 가변(mutable) : 값을 바꿀 수 있음
# 불변(immutable) : 값을 바꿀 수 없음
# 결론 : 튜블은 불변(immutable)이라서 값을 바꿀수 없다






