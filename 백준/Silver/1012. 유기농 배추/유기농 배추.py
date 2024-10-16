from collections import deque

t = int(input())

def bfs(i, j): # 세로랑 가로
    q = deque()
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    q.append([i, j])
    while q:
        i, j = q.popleft()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]

            if ni < 0 or ni > n or nj < 0 or nj > m:
                continue

            if field[ni][nj] == 1:
                q.append([ni, nj])
                field[ni][nj] = 0

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 위치 개수
    cabbage = [list(map(int, input().split())) for _ in range(k)]
    field = [[0] * (m + 1) for _ in range(n + 1)]
    cnt = 0

    for j, i in cabbage:
        field[i][j] = 1

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                field[i][j] = 0
                bfs(i, j)
                cnt += 1
                
    print(cnt)