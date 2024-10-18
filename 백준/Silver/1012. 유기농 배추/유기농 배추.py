from collections import deque

t = int(input())

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()

    q.append([x, y])
    while q:
        j, i = q.popleft()

        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]

            if ni > n or ni < 0 or nj > m or nj < 0:
                continue

            if ground[ni][nj] == 1:
                ground[ni][nj] = 0
                q.append([nj, ni])

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추개수
    cabbage = [list(map(int, input().split())) for _ in range(k)]
    ground = [[0] * (m + 1) for _ in range(n + 1)]
    ans = 0

    for x, y in cabbage:
        ground[y][x] = 1

    for y in range(n):
        for x in range(m):
            if ground[y][x] == 1:
                ground[y][x] = 0
                bfs(x, y)
                ans += 1

    print(ans)