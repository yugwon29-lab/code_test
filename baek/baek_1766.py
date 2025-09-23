# 1766. 문제집
import heapq

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
deg = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    deg[b] += 1

pq = []
for i in range(1, N+1):
    if deg[i] == 0:
        heapq.heappush(pq, i)

result = []
while pq:
    now = heapq.heappop(pq)
    result.append(now)
    for g in edges[now]:
        deg[g] -= 1
        if deg[g] == 0:
            heapq.heappush(pq, g)

print(*result)