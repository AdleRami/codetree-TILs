n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = -1
for i in range(n):
    for j in range(n-2):
        for k in range(i+1,n-1):
            for l in range(n-2):
                ans = max(ans, arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[k][l]+arr[k][l+1]+arr[k][l+2])

print(ans)