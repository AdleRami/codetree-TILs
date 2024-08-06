#객체 선언
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

#변수 입력
n = int(input())

students = []
for _ in range(n):
    name, kor, eng, math = tuple(input().split())
    students.append(Student(name, int(kor), int(eng), int(math)))

#국어, 영어순으로 정렬
students.sort(key = lambda x: (-x.kor, -x.eng, -x.math))

#출력
for i in range(n):
    print(students[i].name, students[i].kor, students[i].eng, students[i].math)