n = int(input())
move = [input().split() for _ in range(n)]

dx,dy = [1,0,-1,0],[0,-1,0,1]
dict_dir={
    'N': 0,
    'W': 1,
    'S': 2,
    'E': 3
}
nx,ny = 0,0
cnt = 0

for i in move:
    for j in range(int(i[1])):
        nx += dx[dict_dir[i[0]]]
        ny += dy[dict_dir[i[0]]]
        cnt += 1
        if nx==0 and ny ==0:
            print(cnt)
            exit()

print(-1)