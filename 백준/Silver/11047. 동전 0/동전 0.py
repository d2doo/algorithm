n, k = map(int, input().split()) # m개의 동전 가치, 만들어야 하는 값
coins = [int(input()) for _ in range(n)]
ans = 0

coins.sort(reverse=True)

for coin in coins:
    if k < coin:
        continue
    else:
        ans += k // coin
        k %= coin

print(ans)