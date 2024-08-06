#객체 선언
class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

#변수 입력
n = int(input())

students = []
for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h,w,i+1))

#조건에 따라 정렬
students.sort(key = lambda x: (-x.height, -x.weight, x.number))

for i in range(n):
    print(students[i].height, students[i].weight, students[i].number)