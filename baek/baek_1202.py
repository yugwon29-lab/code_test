# 1202. 보석 도둑
import heapq

N, K = map(int, input().split())
jewel = []
bag = []

for _ in range(N):
    weight, value = map(int, input().split())
    jewel.append((weight, value))

for _ in range(K):
    b = int(input())
    bag.append(b)

jewel.sort()
bag.sort()

max_value = 0
idx = 0
max_jewel = []
for c in bag:
    while idx < N and jewel[idx][0] <= c:
        heapq.heappush(max_jewel, -jewel[idx][1])
        idx += 1
    if max_jewel:
        max_value += -heapq.heappop(max_jewel)

print(max_value)