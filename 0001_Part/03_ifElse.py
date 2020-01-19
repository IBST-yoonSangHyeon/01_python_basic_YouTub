if(1 > 2):
    print("Hello") #아무것도 출력안됨

if not (1 > 2):
    print("Bye ~ not ")

##조건 여러가지 붙이기
if(1 > 0 and 2 > 1):
    print("Hello")

if(0 > 0 or 2 > 1):
    print("Bye ~ OR")

## ELIF , ELSE 
x = 3 
if( x > 5):
    print("Hello")
elif (x == 3):
    print("Bye ~~~ ")
else:
    print("Hi") 