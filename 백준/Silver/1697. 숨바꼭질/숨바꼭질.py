from collections import deque

n, k = map(int, input().split())
MAX = 100000
time = [-1] * (MAX + 1)
q = deque()

def bfs(n, k):
    time[n] = 0
    q.append(n)

    while q:
        tmp = q.popleft()

        if tmp == k:
            return time[tmp]

        for i in tmp - 1, tmp + 1, tmp * 2:
            if 0 <= i <= MAX and time[i] == -1:
                time[i] = time[tmp] + 1
                q.append(i)

print(bfs(n, k))