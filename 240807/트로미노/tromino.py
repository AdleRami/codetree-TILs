n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def L_grid_sum(x,y):
    max_gold = 0

    #기준점 왼, 위
    if in_range(x,y-1) and in_range(x-1,y):
        max_gold = max(arr[x][y-1] + arr[x-1][y] + arr[x][y], max_gold)

    #기준점 위, 오른
    if in_range(x-1,y) and in_range(x, y+1):
        max_gold = max(arr[x-1][y] + arr[x][y+1] + arr[x][y], max_gold)
    
    #기준점 오른, 아래
    if in_range(x,y+1) and in_range(x+1,y):
        max_gold = max(arr[x][y+1] + arr[x+1][y] + arr[x][y], max_gold)
    
    #기준점 아래, 왼
    if in_range(x+1,y) and in_range(x,y-1):
        max_gold = max(arr[x+1][y] + arr[x][y-1] + arr[x][y], max_gold)
    
    return max_gold

def line_grid_sum(x,y):
    max_gold = 0

    #세로일 경우
    if in_range(x+2, y):
        max_gold = max(arr[x][y] + arr[x+1][y] + arr[x+2][y], max_gold)
    
    #가로일 경우
    if in_range(x,y+2):
        max_gold = max(arr[x][y] + arr[x][y+1] + arr[x][y+2], max_gold)

    return max_gold

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, L_grid_sum(i,j), line_grid_sum(i,j))

print(ans)