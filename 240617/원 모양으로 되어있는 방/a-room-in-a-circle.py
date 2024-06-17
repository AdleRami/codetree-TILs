import sys

INT_MAX = sys.maxsize

n = int(input())
room = [int(input()) for _ in range(n)]

ans = INT_MAX

#i번째 방부터 시작
for i in range(n):
    dist = 0
    for j in range(n):
        cnt = (j+n-i)%n #원의 인덱스 표현 방법 참고
        dist += cnt * room[j]

    ans = min(ans,dist)

print(ans)