def check(N, M):
    max_day = -1  # 마지막으로 토마토가 익은 날
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 0:  # 익은 토마토가 있는 경우
                if max_day < visited[i][j]:
                    max_day = visited[i][j]
            elif tomato[i][j] == 0 and visited[i][j] == -1:  # 안익은 토마토가 남은 경우
                return -1
    return max_day

from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
# bfs 익혀보기...
q = deque()     # 큐 생성
visited = [[-1]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:     # 처음에 익은 토마토인 경우
            q.append((i,j))
            visited[i][j] = 0
while q:
    i, j = q.popleft()          # 익은 토마토 좌표를 꺼내
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i+di, j+dj # 익은 토마토 주변에서 안익은 토마토였고, 여전히 익지않았다면
        if 0<=ni<N and 0<=nj<M and tomato[ni][nj]==0 and visited[ni][nj]==-1:
            q.append((ni,nj))
            visited[ni][nj] = visited[i][j] + 1


print(check(N, M))