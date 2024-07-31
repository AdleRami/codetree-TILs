n, t = tuple(map(int,input().split()))
r,c,d = tuple(input().split())

dir_x,dir_y = [1,0,-1,0],[0,1,0,-1]
dict_dir={  #방향 딕셔너리 선언
    'R': 1,
    'U': 2,
    'L': 3,
    'D': 0
}

def in_range(x,y):
    return 0<=x<n and 0<=y<n

ans_x,ans_y,move = int(r)-1,int(c)-1,dict_dir[d]

for _ in range(t):
    nx,ny = ans_x + dir_x[move],ans_y+dir_y[move]
    if in_range(nx,ny):
        ans_x,ans_y = nx,ny
    else:
        move = (move+2) % 4

print(ans_x+1,ans_y+1)