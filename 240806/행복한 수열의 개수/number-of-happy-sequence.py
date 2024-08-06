n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def row_happy(x):
    check_happy_num = arr[x][0]
    
    max_cnt = 0
    cnt = 0
    for i in range(1,n):
        if check_happy_num == arr[x][i]:
            cnt += 1            
            max_cnt = max(max_cnt,cnt)
        else:
            check_happy_num = arr[x][i]            
            max_cnt = max(max_cnt,cnt)
            cnt = 0
    
    return max_cnt

def cul_happy(x):
    check_happy_num = arr[0][x]

    max_cnt = 0
    cnt = 0
    for i in range(1,n):
        
        if check_happy_num == arr[i][x]:
            cnt += 1
            max_cnt = max(max_cnt,cnt)
        else:
            check_happy_num = arr[i][x]
            max_cnt = max(max_cnt,cnt)
            cnt = 0
        
    
    return max_cnt

num_happy = 0
for i in range(n):
    row_happy_num, cul_happy_num = row_happy(i), cul_happy(i)
    #print(row_happy_num, cul_happy_num)
    if row_happy_num >= m-1:
        num_happy += 1
    if cul_happy_num >= m-1:
        num_happy += 1  

print(num_happy)