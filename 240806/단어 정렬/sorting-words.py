#n 입력 및 string 입력
n = int(input())
string_list = [input() for _ in range(n)]

#배열 정렬
string_list.sort()

#출력
for i in string_list:
    print(i)