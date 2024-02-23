from collections import deque
N, M = map(int, input().split())
lst = deque(range(1, N + 1))
answer = []

while lst: # 원처럼 삥글뺑글 돌려버리기
    for _ in range(M-1): # M번째 보다 하나 전까지 요소 돌리고
        lst.append(lst.popleft()) # 첫 요소를 빼고 뒤로 붙여
    answer.append(lst.popleft()) # M번째 요소는 answer에 넣어

# res = ', '.join(map(str, answer))
print(str(answer).replace('[', '<').replace(']', '>'))