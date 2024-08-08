n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def rect_sum(x,y,k,l):
    #가야하는 방향의 dx,dy
    dx, dy = [-1,-1,1,1],[1,-1,-1,1]
    #한쪽 방향으로 움직이는 횟수
    move_num = [k,l,k,l]

    sum_of_nums=0

    for dx, dy, move_num in zip(dx, dy, move_num):
        for _ in range(move_num):
            x,y = x+ dx, y + dy

            if not in_range(x,y):
                return 0

            sum_of_nums += grid[x][y]
    
    return sum_of_nums

ans = 0

for i in range(n):
    for j in range(n):
        for k in range(1,n):
            for l in range(1,n):
                ans = max(ans, rect_sum(i, j, k , l))

print(ans)