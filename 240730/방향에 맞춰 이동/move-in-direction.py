n = int(input())
move = [input().split() for _ in range(n)]

dx,dy = [1,-1,0,0], [0,0,1,-1]
x,y = 0, 0
for i in range(n):
    if move[i][0] == 'N':
        x += int(move[i][1])*dx[2]
        y += int(move[i][1])*dy[2]

    elif move[i][0] == 'S':
        x += int(move[i][1])*dx[3]
        y += int(move[i][1])*dy[3]

    elif move[i][0] == 'E':
        x += int(move[i][1])*dx[0]
        y += int(move[i][1])*dy[0]
    
    else:        
        x += int(move[i][1])*dx[1]
        y += int(move[i][1])*dy[1]

print(x,y)