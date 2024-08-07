import itertools

#변수 입력
n = int(input())
arr = list(map(int,input().split()))

#arr 정렬
arr.sort()

group_max = 0
for i in range(n):
    # i번째와 2n - 1 - i번째 원소를 매칭합니다. 정렬 후 
    #print(i, 2*n - 1 - i)
    group_sum = arr[i] + arr[2*n - 1 - i]
    if group_sum > group_max:
        # 최댓값을 갱신합니다.
        group_max = group_sum

print(group_max)