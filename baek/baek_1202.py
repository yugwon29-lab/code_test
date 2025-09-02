# 1202. 보석 도둑
N, K = map(int, input().split())

jewel = []
for _ in range(N):
    M, V = map(int, input().split())
    jewel.append((V, M))

bag = []
for _ in range(K):
    C = int(input())
    bag.append(C)

jewel.sort(reverse=True)
bag.sort()

used = [False] * K
total_value = 0

for j in jewel:
    value, mass = j[0], j[1]
    idx = 0
    while True:
        if idx >= K or bag[idx] < mass:
            break
        idx += 1
    while idx < K and used[idx]:
        idx += 1
    if idx >= K:
        continue
    total_value += value
    used[idx] = True

print(total_value)

