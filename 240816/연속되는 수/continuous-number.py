n = int(input())
arr = list(int(input()) for _ in range(n))

set_arr = set(arr)
ans = 0

for del_num in set_arr:
    del_arr = [i for i in arr if i != del_num]
    #print(del_arr)
    seq_num = del_arr[0]

    cnt = 0
    for i in range(1,len(del_arr)):
        if seq_num == del_arr[i]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            seq_num = del_arr[i]
            cnt = 0

print(ans+1)