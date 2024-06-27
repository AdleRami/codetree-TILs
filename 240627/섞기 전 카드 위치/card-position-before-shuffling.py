n = int(input())
shuffle = list(map(int,input().split()))
card = list(map(int,input().split()))

ans = card
for i in range(3):
    tmp = ans
    tmp_num = ans[0]
    for j in range(len(shuffle)):        
        ans[j] = tmp[shuffle[j]-1]
        if j == 4:
            ans[j] = tmp_num
        
for i in ans:
    print(i)