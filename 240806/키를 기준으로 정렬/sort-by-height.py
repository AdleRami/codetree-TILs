#객체 선언
class person:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

#변수 입력
n = int(input())

people = []
for _ in range(n):
    name, height, weight = input().split()
    people.append(person(name,height,weight))

#키 순으로 정렬
people.sort(key = lambda x: x.h)

#출력
for i in range(n):
    print(people[i].n, people[i].h, people[i].w)