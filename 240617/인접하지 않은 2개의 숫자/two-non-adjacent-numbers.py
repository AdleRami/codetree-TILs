import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

ans = INT_MIN
for i in range(n-2):
    sum_min = 0
    for j in range(i+2, n):
        sum_min = arr[i]+arr[j]
    
    ans = max(ans,sum_min)

print(ans)