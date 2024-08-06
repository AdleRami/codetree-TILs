#n, k, T 입력
n, k, T = tuple(input().split())

#단어 리스트 입력
string_list = [input() for _ in range(int(n))]

#string_list 정렬
string_list.sort()

#T로 시작하는 단어 새로운 배열에 append
T_string = []
for i in string_list:
    if i[:len(T)] == T:
        T_string.append(i)

print(T_string[int(k)-1])