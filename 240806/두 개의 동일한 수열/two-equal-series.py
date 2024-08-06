#n 및 변수 입력
n = int(input())
A = list(map(int, input().split()))
B = list(map(int,input().split()))

#A,B 일치 여부를 위해 정렬
A.sort()
B.sort()

#일치 여부 판단
if A == B:
    print('Yes')
else:
    print('No')