n, m = map(int, input().split())
draw = [list(map(int,input().split())) for _ in range(m)]
draw_map = [[0]*n for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def check_comfortable(x,y):
    global draw_map

    dx,dy = [0,1,0,-1],[1,0,-1,0]

    cnt = 0
    for i in range(4):
        check_x,check_y = x + dx[i], y+ dy[i]
        if in_range(check_x,check_y) and draw_map[check_x][check_y] == 1:
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)

for i in draw:
    nx,ny = i[0]-1, i[1]-1
    draw_map[nx][ny] = 1

    check_comfortable(nx,ny)