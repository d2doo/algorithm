n, k = map(int, input().split()) # m개의 동전 가치, 만들어야 하는 값
coins = []
ans = 0

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
    if k < coin:
        continue
    else:
        ans += k // coin
        k %= coin

print(ans)