# 자료구조(Structure)의 리스트(List) 구조
# 리스트는 엘리멘터리 여러개를 그룹핑할때 사용하는 것이다.
# 리스트 기본
# 리스트 자주 사용하는 함수
# 리스트를 반복문으로 출력 
# 리스트에서 엘리먼트 위치 찾기


## 리스트 기본
# list() == [] 
x = list()
y = [] 

print(x)
print(y)

x = [1, 2, 3, 4]
y = ["hello", "world"]
z = ["hello", 1, 2, 3] #다른 타입 합치는 것도 가능함

print(x + y) # 리스트 끼리 합치는거 가능
print(x[0])
print(x[3])

x[3] = 10 #엘리멘트 값 바꾸는것 가능
print(x)

#print(x[4]) #Error !!! 리스트에서 벗어난 인덱스 출력시 에러가남

## 리스트 자주 사용하는 함수
# 리스트에서 제공하는 자주 사용하는 대표 함수들

# len 함수 : 엘리먼트 길이 구함
x = [1, 2, 3, 4]

num_elements = len(x) 
print(num_elements)

# sorted 함수 : 엘리먼트 정렬 처리함
x = [4, 2, 3, 1]

y = sorted(x)
print(y)

# sun 함수 : 합계를 구함
x = [4, 2, 3, 1, int("1")]

z = sum(x)
print(z)

## 리스트를 반복문으로 출력 
x = [4, 2, 3, 1]
y = ["hello", "there"]

for n in x:
    print(n)

for c in y:
    print(c)

##리스트에서 엘리먼트 위치 찾기
x = [4, 2, 3, 1]
y = ["hello", "there"]

# index 함수 : 엘리먼트 위치를 찾아 줌
print(x.index(3))
print(y.index("hello"))
#print(y.index(10)) #Error !!! 리스트에 없다고 에러남

# in 키워드 : 어떤 엘리먼트에 있는지만 체크하고 싶다
print("hello" in y) # True 출력
print("bye" in y) # False 출력

if "hello" in x:
    print("hello 가 있어요")




