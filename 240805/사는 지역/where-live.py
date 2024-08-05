#클래스 선언
class citizen:
    def __init__(self, name, street_number, region):
        self.name = name
        self.street = street_number
        self.region = region

#n 값 입력 및 변수 입력
n = int(input())

people = []
for i in range(n):
    citizen_name, street_number, region = tuple(input().split())
    people.append(citizen(citizen_name, street_number, region))

#람다 함수를 이용한 정렬
sorted_people = sorted(people, key = lambda x: x.name)

print(f"name {sorted_people[n-1].name}")
print(f"addr {sorted_people[n-1].street}")
print(f"city {sorted_people[n-1].region}")