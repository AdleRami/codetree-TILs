class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


students = []
for _ in range(5):
    name, h, w = tuple(input().split())
    students.append(Student(name, int(h), float(w)))

students.sort(key = lambda x: x.name)
print('name')
for i in range(5):
    print(students[i].name, students[i].height, students[i].weight)

print()
students.sort(key = lambda x : -x.height)
print('height')
for i in range(5):
    print(students[i].name, students[i].height, students[i].weight)