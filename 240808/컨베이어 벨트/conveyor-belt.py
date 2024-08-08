n, t = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]

for second in range(t):

    #첫번째 줄에서 n번째 숫자 저장
    belt_temp1 = belt[0][n-1]
    #두번째 줄에서 n번째 숫자 저장
    belt_temp2 = belt[1][n-1]

    for i in range(n-1, 0, -1):
        #첫번째 줄 밀기
        belt[0][i] = belt[0][i-1]

        #2번째 줄 밀기
        belt[1][i] = belt[1][i-1]

    belt[1][0] = belt_temp1
    belt[0][0] = belt_temp2


#belt 출력
for i in range(2):
    for j in range(n):
        print(belt[i][j], end = ' ')
    print()