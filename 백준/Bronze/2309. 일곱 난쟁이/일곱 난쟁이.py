arr = []
for i in range(9):
    arr.append(int(input()))

# print(arr) # [20, 7, 23, 19, 10, 15, 25, 8, 13]

arr.sort()
sumarr = sum(arr)
clue = sumarr - 100

# print(clue) # 40

from itertools import combinations

lst = list(combinations(arr, 2))
m = len(lst)
for i in range(m):
    # print(lst[i])
    cnt = 0
    for j in range(2):
        cnt += lst[i][j]
    if cnt == clue:
        a, b = lst[i]

for i in arr:
    if i != a:
        if i != b:
            print(i)