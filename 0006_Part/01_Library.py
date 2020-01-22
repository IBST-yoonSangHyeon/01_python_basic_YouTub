# 라이브러리, API
# 라이브러리 == 다른 개발자가 자기 패키지를 공개해 놓은것 
# API == 서비스 제공자가 우리같은 우리 같은 개발자들이 코드를 통해서 데이터를 가져 갈수 있도록 만들어 놓은 길

# twilio API 사용



## twilio API 사용
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

#Acount 번호
account_sid = '<Acount 번호>'
#인증 토큰 
auth_token = '<인증 토큰>'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     # 문자 내용
                     body="안녕하세요!!! 반갑습니다~",
                     # 발신 번호
                     from_='<발신 번호>',
                     to='<수신자 번호>' 
                     # EX) +82(국제전화번호:대한민국) 핸드폰번호 (010-1234-1234 번호에서 하이픈 빼고, 맨앞 0 뺄것)
                     # +821012341234
                 )

print(message.sid)
