# 24445. DFS와 BFS
from collections import deque

N, M, V = map(int, input().split())

# 그래프
graphs = [[] for _ in range(N+1)]
dfs = [0] * (N+1)
bfs = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

for g in graphs:
    g.sort(reverse=True)

start = V
queue = deque()

queue.append(start)
dfs_visit = []

while queue:
    now = queue.pop()
    if not dfs[now]:
        dfs[now] = 1
        dfs_visit.append(now)
        for next in graphs[now]:
            if not dfs[next]:
                queue.append(next)

print(*dfs_visit)

for g in graphs:
    g.sort()

start = V
queue = deque()

queue.append(start)
bfs[start] = 1
bfs_visit = []

while queue:
    now = queue.popleft()
    bfs_visit.append(now)
    for c in graphs[now]:
        if not bfs[c]:
            queue.append(c)
            bfs[c] = 1

print(*bfs_visit)
