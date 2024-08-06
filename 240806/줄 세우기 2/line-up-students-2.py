class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

students = []
n = int(input())

for i in range(n):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, i+1))

students.sort(key = lambda x: (x.height, -x.weight))

for i in range(n):
    print(students[i].height, students[i].weight, students[i].number)