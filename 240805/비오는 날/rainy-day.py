#클래스 선언
class weather_forcast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

#n 값 입력 및 변수 입력
n = int(input())

weather_list = []
for i in range(n):
    date, day, weather = tuple(input().split())
    weather_list.append(weather_forcast(date, day, weather))

#날짜 순으로 정렬하기
sorted_weather_list = sorted(weather_list, key = lambda x: x.date)
#처음으로 비내리는 날 찾기
rain_idx = 0
for i in range(n):
    if sorted_weather_list[i].weather == 'Rain':
        rain_idx = i
        break

print(sorted_weather_list[i].date, sorted_weather_list[i].day, sorted_weather_list[i].weather)