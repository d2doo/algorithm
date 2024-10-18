# 회의실 배정

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]

meeting.sort(key= lambda x: (x[1], x[0]))

ans = 1
end = meeting[0][1]
for i in range(1, n):
    if meeting[i][0] >= end:
        ans += 1
        end = meeting[i][1]

print(ans)