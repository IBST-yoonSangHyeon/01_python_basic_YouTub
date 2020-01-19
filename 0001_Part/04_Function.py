# 간단하게 설명하면 
# 함수란 반복되는 코드를 그룹으로 나눈것이라함
# 합수생성시 키워드 def(define) 사용함

## 결과 print
def chat(name1, name2, age):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 %d살" % (name2, age))

chat("알렉스", "윤하", 10)
chat("철수", "영희" , 30)

## 결과 return
def dsum(a, b):
    result = a + b
    print(result)
    return result

d = dsum(1, 2) 
print(d) #만약 retrurn 결과 값이 없다면 None 이라고 뜸 (알아두자 에러는 아니기에 실행됨)


