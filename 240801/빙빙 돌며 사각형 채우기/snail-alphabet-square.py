n,m = map(int, input().split())

arr = [[0]*m for _ in range(n)]
arr[0][0] = 'A'
dir_num = 0

dx,dy = [0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x<m and 0<=y<n

x,y = 0,0
for i in range(ord('B'), ord('B') + n*m-1):
    nx,ny = x + dx[dir_num],y +dy[dir_num]
    if not in_range(nx,ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x,y = x + dx[dir_num], y + dy[dir_num]
    arr[x][y] = chr(i)

for i in range(n):
    for j in range(m):
        print(arr[i][j],end = ' ')
    print()