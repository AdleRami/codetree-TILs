import sys
from itertools import combinations


INT_MAX = sys.maxsize
n,s = map(int,input().split())
arr = list(map(int, input().split()))

comb = list(combinations(arr,len(arr)-2))

min_abs = INT_MAX
for i in range(len(comb)):
    min_abs = min(min_abs,abs(sum(comb[i])-s))

print(min_abs)