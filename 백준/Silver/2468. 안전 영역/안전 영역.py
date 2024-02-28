from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 최댓값 갱신하는 코드
max_v = 0
for i in range(N):
    max_v = max(max_v, max(arr[i]))

# bfs 코드
def bfs(i, j, a):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > a and not visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = 1

# 문제 구현
max_cnt = 0
for a in range(max_v):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > a and not visited[i][j]:
                bfs(i, j, a)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)