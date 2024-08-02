n = int(input())
start_point_x,start_point_y = n//2, n//2
arr = [[0]*n for _ in range(n)]
arr[start_point_x][start_point_y] = 1
dx, dy = [0,-1,0,1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

x,y = n//2,n//2
dir_num = 0
for i in range(2,n**2+1):
    nx, ny = x + dx[dir_num], y + dy[dir_num]

    if in_range and arr[nx][ny] == 0:
        arr[nx][ny] = i
        if arr[nx + dx[(dir_num+1) % 4]][ny+ dy[(dir_num+1) % 4]] == 0:
            dir_num = (dir_num+1) % 4
        else:
            dir_num = dir_num
        x,y = nx, ny

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()