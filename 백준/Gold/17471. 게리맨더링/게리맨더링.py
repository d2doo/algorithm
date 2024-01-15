def f(g, N): # 선거구를 탐색하는 bfs()
    q = [g[0]] # 시작점 인큐
    v = [0] * (N + 1) # visited 생성
    v[g[0]] = 1 # 시작점 방문 표시
    cnt = 0
    while q:
        t = q.pop(0)
        cnt += 1
        for i in adjl[t]:
            if i in g and v[i] == 0:
                q.append(i)
                v[i] = 1
    if len(g) ==cnt:
        return 1
    else:
        return 0

N = int(input())
population = list(map(int, input().split()))
adjl = [[]]
for i in range(N):
    tmp = list(map(int, input().split()))
    adjl.append(tmp[1:])

arr = [i for i in range(1, N+1)]
min_v = 1000
for i in range(1, (1<<N)//2):
    a = []
    b = []
    pa = pb = 0
    for j in range(N):
        if i&(1<<j):
            a.append(arr[j]) # a 그룹에 속한 구역 번호
            pa += population[j] # a 그룹의 인구 합계
        else:
            b.append(arr[j]) # b 그룹에 속한 구역 번호
            pb += population[j] # b 그룹의 인구 합계
    r1 = f(a, N)
    r2 = f(b, N)
    if r1 and r2: # A, B 둘 다 정상인 경우
        if min_v > abs(pa-pb):
            min_v = abs(pa-pb)

if min_v == 1000:
    min_v = -1

print(min_v)