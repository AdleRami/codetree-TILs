class Point:
    def __init__(self, x, y, number, distance):
        self.x = x
        self.y = y
        self.number = number
        self.distance = distance

def distance(x,y):
    return abs(0-x) + abs(0-y)

n = int(input())

points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append(Point(x,y,i+1,distance(x,y)))

points.sort(key = lambda x : (x.distance, x.number))

for i in range(n):
    print(points[i].number)