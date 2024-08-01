move = input()

dx,dy = [0,1,0,-1],[1,0,-1,0]
time = 0
nx,ny = 0,0
move_dir = 0

for i in move:
    if i == 'L':
        move_dir = (move_dir-1+4) % 4
        time += 1
    elif i == 'R':
        move_dir = (move_dir+1) % 4
        time += 1
    else:
        nx += dx[move_dir]
        ny += dy[move_dir]
        time += 1
    
    if nx == 0 and ny == 0:
        print(time)
        exit()

print(-1)