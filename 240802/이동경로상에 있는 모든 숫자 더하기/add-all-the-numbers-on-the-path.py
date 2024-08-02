n,t = map(int, input().split())
move = input()
arr = [list(map(int,input().split())) for _ in range(n)]

star_point_x, star_point_y = n//2, n//2

dx,dy = [-1,0,1,0], [0,1,0,-1]
x,y = star_point_x,star_point_y
ans = arr[star_point_x][star_point_y]
dir_num = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

for i in move:
    if i == 'L':
        dir_num = (dir_num-1+4) % 4
    elif i == 'R':
        dir_num = (dir_num+1) % 4
    else:
        nx, ny = x + dx[dir_num], y + dy[dir_num]
        if in_range(nx,ny):
            ans += arr[nx][ny]
            x,y = nx,ny
        else:
            continue

print(ans)