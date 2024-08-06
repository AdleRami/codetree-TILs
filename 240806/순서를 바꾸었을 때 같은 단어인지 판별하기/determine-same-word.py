#변수 입력
string1 = input()
string2 = input()

#두 list 정렬
sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)

#두 list 일치 판별
if sorted_string1 == sorted_string2:
    print('Yes')
else:
    print('No')