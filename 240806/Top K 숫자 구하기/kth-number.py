#n, k, 숫자 입력
n, k = map(int, input().split())
arr = list(map(int, input().split()))

#숫자 정렬
arr.sort()

#k번째 수 출력
print(arr[k-1])