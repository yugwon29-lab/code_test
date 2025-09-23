# 2252. 줄 세우기
from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
in_degrees = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    in_degrees[b] += 1

queue = deque()
for i in range(1, N+1):
    if in_degrees[i] == 0:
        queue.append(i)

result = []

while queue:
    now = queue.popleft()
    result.append(now)
    for g in edges[now]:
        in_degrees[g] -= 1
        if in_degrees[g] == 0:
            queue.append(g)

print(*result)