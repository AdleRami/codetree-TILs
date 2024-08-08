n, m =map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def check_positive_rect(x1, y1, x2, y2):
    rect_size = 0

    #(x,y)의 좌표가 음수면 0을 리턴
    if grid[x1][y1] < 0:
        return 0
    
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):

            #(i,j)의 숫자가 음수면 0을 리턴
            #(i,j)의 숫자가 양수면 size를 증가
            if grid[i][j] < 0:
                return 0
            else:
                rect_size += 1
    
    return rect_size

ans = 0

for x1 in range(n):
    for y1 in range(m):
        for x2 in range(x1,n):
            for y2 in range(y1,m):
                ans = max(ans, check_positive_rect(x1, y1, x2, y2))

print(ans)