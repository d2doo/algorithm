#백준 숨바꼭질
def bfs(N, K):
    # N에서 K에 도착하는 최단시간 출력...
    q = []  # 큐 생성
    q.append(N)  # 시작점 인큐
    visited = [-1] * 100001  # visited 생성
    visited[N] = 0 # 시작점 표시

    while q: # 큐가 비워질 때 까지...
        t = q.pop(0) # t <- 디큐
        if t == K: # t == k 인 경우 종료...
            return visited[t]

        if t > 0 and visited[t-1] == -1: # t에 인접인... t-1, t+1, t*2 위치가 아직 방문한 적 없으면
            q.append(t - 1) # 인큐하고 visited 표시
            visited[t - 1] = visited[t] + 1

        if t < 100000 and visited[t + 1] == -1:
            q.append(t + 1)
            visited[t + 1] = visited[t] + 1

        if t * 2 <= 100000 and visited[t * 2] == -1:
            q.append(t * 2)
            visited[t * 2] = visited[t] + 1




N, K = map(int, input().split())
print(bfs(N, K))    # N에서 K에 도착하는 최단시간 출력


