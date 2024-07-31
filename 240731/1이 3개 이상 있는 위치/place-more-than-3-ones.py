n = int(input())
arr = [list(map(int, input().split()) for _ in range(n))]
dir_x, dir_y = [0,1,0,-1],[1,0,-1,0]
cnt = 0

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def adjacent_cnt(x,y):
    cnt = 0
    for dx,dy in zip(dir_x,dir_y):
        nx,ny = x + dx, y + dy
        if in_range(nx,ny) and arr[nx,ny] == 1:
            cnt+=1
    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i,j) >=3:
            ans+=1

print(ans)