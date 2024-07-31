move = input()
dir_x, dir_y = [0,1,0,-1],[1,0,-1,0]
index = 0
x, y = 0, 0

for i in move:    
    if i == 'L':
        index = (index+3) % 4
    elif i == 'R':
        index = (index+1) % 4
    else:
        x, y = x + dir_x[index] , y + dir_y[index]

print(x,y)