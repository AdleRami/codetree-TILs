class Number:
    def __init__(self, number, index):
        self.number = number
        self.index = index

n = int(input())
num_list = list(map(int, input().split()))

nums = []
for idx, number in enumerate(num_list,start = 1):
    nums.append(Number(number, idx))

nums.sort(key = lambda x: (x.number, x.index))


for i in range(1, n+1):
    for j in range(len(nums)):
        if i == nums[j].index:
            print(j+1, end = ' ')