# 타입은 크게 
# 숫자, 문자, 불리언 3가지로 나뉨

##숫자 

x = 1
y = 2
z = 1.2 

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x ** y) #제곱
print(x % y)  #나머지(mod)


##문자열 
x = "hello"
y = 'bye' 

#엔터키 포함된 문자열
z = """
안녕하세요
윤상현입니다.
"""
print(x)
print(y)

print(z)

#사칙연산으로 문자열 처리 가능
print("너 혹시 몇 살이니? " + "난 4 살")
#서로 다른 타입 사칙연산
#print("너 혹시 몇 살이니?" + 4)#Error 다른 타입으로 사칙연산 불가!!!
print("너 혹시 몇 살이니? " + str(4))#(캐스팅(casting) 해야함)

x = 4 # 숫자 타입
y = "4" # 문자열 타입

print(str(x) + y)
print(x + int(y))

##불리언(True/False)
x = True
y = False

print(x)
print(y)







