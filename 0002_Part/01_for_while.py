#반복문은 크게 for, while 문이 있음
#break , continue

## for 문
for i in range(3):
    print(i) # 0
    print("철수 : 안녕 영희야 뭐해?")
    print("영희 : 안녕 철수야, 그냥 있어.")

## while 문 (for문과 다른점은 조건문 사용가능함)
i = 0
while i < 3:
    print(i) # 0
    print("철수 : 안녕 영희야 뭐해?")
    print("영희 : 안녕 철수야, 그냥 있어.")
    # 파이썬은 일관성과 가독성을 위한 언어이므로 증감연산자 제공안함
    i = i + 1

# 사용하는 경우에 따라 for문, while문 쓰는경우가 달라진다.
# 둘을 비교하여 굳이 다른점은 무한 반복문이다.


## brake
# 무한반복
i = 0
while True:
    print(i) # 0
    print("철수 : 안녕 영희야 뭐해??")
    print("영희 : 안녕 철수야, 그냥 있어..")
    # 파이썬은 일관성과 가독성을 위한 언어이므로 증감연산자 제공안함
    i = i + 1

    if i > 2:
        break

for i in range(100):
    print(i) # 0
    print("철수 : 안녕 영희야 뭐해???")
    print("영희 : 안녕 철수야, 그냥 있어...")
    # 파이썬은 일관성과 가독성을 위한 언어이므로 증감연산자 제공안함
    i = i + 1

    if i > 2:
        break

## continue
for i in range(3):
    print(i) # 0
    print("철수 : 안녕 영희야 뭐해????")
    print("영희 : 안녕 철수야, 그냥 있어....")

    continue

    print("상현 : 안녕 영희야 뭐해????")

