n = int(input())
move = [list(input().split()) for _ in range(n)]
x,y = 0,0

direction = ['E','W','S','N']
dxs,dys = [1,-1,0,0],[0,0,-1,1]

for i in range(n):
    x += dxs[direction.index(move[i][0])] * int(move[i][1])
    y += dys[direction.index(move[i][0])] * int(move[i][1])

print(x,y)