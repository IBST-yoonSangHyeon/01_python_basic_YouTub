# 외부 패키지 사용
# 외부 패키지 사용 및 구현


## 외부패키지 사용 및 구현

# from animal.dog import Dog # 이거랑 같음

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="yoonsanhyeon")
location = geolocator.geocode("Seoul, South Korea")
print(location)
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)