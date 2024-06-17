import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
binary = list(map(int, list(input())))

ans = INT_MIN
for i in range(len(binary)):
    binary[i] = 1 - binary[i]

    num = 0
    for j in range(len(binary)):
	    num += (2**(j)) * binary[len(binary)-1-j]
    
    ans = max(ans,num)

    #바꿔준 바이너리 원래대로
    binary[i] = 1 - binary[i]

print(ans)