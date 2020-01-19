# 자료구조(Structure)의 딕셔너리(Dictionary) 구조

# 딕셔너리 기본
# 딕셔너리 사용법 
# 딕셔너리도 리스트 처럼 가능한것들
# 딕셔너리의 유용한 함수들
# 딕셔너리 반복문 
# 딕셔너리도 Assignment 가능 

## 딕셔너리 기본
x = dict()
y = {}

print(x)
print(y)

## 딕셔너리 사용법 
# 딕셔너리는 key와 Value로 이루어져 있는 자료구조
x = {
    "name" : "윤상현",
    "age" : 20,
}
print(x)
print(x["name"])
print(x["age"])

# Key값에 들어갈수 있는 것은 불변(immutable) 값만 들어갈수 있음
# 리스트는 "가변"(mutable) 이니까 딕셔너리의 key로 쓸수 없음
x = {
    0 : "Yoon Sang Hyeon",
    1 : "Hello",
    "age" : 2, 
}

print(x[0])
print(x[1])
print(x["age"])

## 딕셔너리도 리스트 처럼 가능한것들
# 어떤 키가 있는지 찾기 가능
print("age" in x) # True
print("name" in x) # True

## 딕셔너리의 유용한 함수들

# keys 함수 : 딕셔너리의 모든 Key 값을 구해줌
print(x.keys())
# values 함수 : 딕셔너리의 모든 Value를 구해줌
print(x.values())

## 딕셔너리 반복문 
x = {
    0 : "Yoon Sang Hyeon",
    1 : "Hello",
    "age" : 2, 
}

for key in x:
    print("key : " + str(key)) # key 값
    print("Value : " + str(x[key])) #Value 값

## 딕셔너리도 Assignment 가능 
x = {
    0 : "Yoon Sang Hyeon",
    1 : "Hello",
    "age" : 2, 
}

# 딕셔너리 값 바꿈
x[0] = "윤상현"
print(x)

# 딕셔너리 값 추가
x["school"] = "한빛"
print(x)




