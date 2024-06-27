n = int(input())

# Before shuffle
location = list(map(int, input().split()))
card = list(map(int, input().split()))


cnt = 0

list_set = []

before_location = [0]*len(location)
for _ in range(3):
    
    for idx, loc in enumerate(location):
        before_location[idx] = card[loc-1]
 
    card = before_location.copy()


for i in card:
	print(i)