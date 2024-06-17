import sys

INT_MAX = sys.maxsize

n = int(input())
check_point = [list(map(int,input().split())) for _ in range(n)]

prev_idx = 0
dist = 0
min_dist = INT_MAX

#i번째 정류장 건너뛰기
for i in range(1,n -1):
    for j in range(1,n):
        if i == j :
            continue
        dist += abs(check_point[prev_idx][0]-check_point[j][0])+abs(check_point[prev_idx][1]-check_point[j][1])
        prev_idx = j
    
    #다 더한것에서 최솟값 구하기
    min_dist = min(dist, min_dist)

print(min_dist)