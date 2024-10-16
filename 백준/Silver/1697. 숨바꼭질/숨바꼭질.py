from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX + 1)
q = deque()

def bfs(n, k):
    visited[n] = 0
    q.append(n)

    while q:
        temp = q.popleft()

        if temp == k:
            return visited[temp]

        for i in temp - 1, temp + 1, temp * 2:
            if 0 <= i <= MAX and visited[i] == -1:
                visited[i] = visited[temp] + 1
                q.append(i)

print(bfs(n, k))