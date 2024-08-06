#n, 숫자 입력
n = int(input())
num = list(map(int, input().split()))

#중앙값 출력을 위한 새로운 배열 선언
ans_list = []
for i in range(n):
    ans_list.append(num[i])
    if i % 2 == 0:
        #홀수 번째의 수까지 정렬 후 출력
        ans_list.sort()
        print(ans_list[len(ans_list)//2], end = ' ')