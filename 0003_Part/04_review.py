# 각 리스트안에 과일이 몇개 있는지 프로그램 짜보자!

fruit = ["사과", "사과", "바나나", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

d = {}

for f in fruit:
    if f in d: # "사과" 라는 key가 d라는 딕셔너리에 들어있어?
        d[f] = d[f] + 1
    else:
        d[f] = 1 # 만약 "사과" 라는 key가 없으면 , 그럼 딕셔너리에 넣고 벨류는 1로 만들어줘

print(d)

# 이러한 분제 대기업에서 짜보라고 함


