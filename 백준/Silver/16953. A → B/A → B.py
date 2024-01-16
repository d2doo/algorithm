def f(n, B, c):
    global min_v
    if n == B:
        if min_v > c:
            min_v = c
    elif n>B:
        return
    else:
        f(n*2, B, c+1)
        f(n*10+1, B, c+1)

A, B = map(int, input().split())
min_v = int(1e9)
f(A, B, 1)
if min_v == int(1e9):
    min_v = -1

print(min_v)