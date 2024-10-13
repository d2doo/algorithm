# 연산자 끼워넣기

def backtracking(idx, now):
    global max_v, min_v

    # 종료조건: 모든 숫자를 다 사용했을 때
    if idx == N - 1:
        max_v = max(now, max_v)
        min_v = min(now, min_v)
        return

    # 덧셈
    if operator[0] != 0:
        operator[0] -= 1  # 가능한 횟수를 빼주고
        backtracking(idx + 1, now + numbers[idx + 1])
        operator[0] += 1

    # 뺄셈
    if operator[1] != 0:
        operator[1] -= 1  # 가능한 횟수를 빼주고
        backtracking(idx + 1, now - numbers[idx + 1])
        operator[1] += 1

    # 곱셈
    if operator[2] != 0:
        operator[2] -= 1  # 가능한 횟수를 빼주고
        backtracking(idx + 1, now * numbers[idx + 1])
        operator[2] += 1

    # 나눗셈
    if operator[3] != 0:
        operator[3] -= 1  # 가능한 횟수를 빼주고
        if now < 0:
            backtracking(idx + 1, -(-now // numbers[idx + 1]))  # 음수 나눗셈 처리
        else:
            backtracking(idx + 1, now // numbers[idx + 1])
        operator[3] += 1

# 입력
N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))

# 초기화
max_v = -1e9  # -10억
min_v = 1e9   # 10억

# 백트래킹 시작
backtracking(0, numbers[0])

# 결과 출력
print(max_v)
print(min_v)
