n,k = map(int, input().split())
arr = list(map(int,input().split()))

ans = -1

for i in range(n-k+1):
    sum_3 = 0
    for j in range(i, i+k):
        sum_3 += arr[j]

    ans = max(ans,sum_3)

print(ans)