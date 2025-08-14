# 24444. 알고리즘 수업 - 너비 우선 탐색 1
from collections import deque

N, M, R = map(int, input().split())

# 그래프
graphs = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

for g in graphs:
    g.sort()

start = R
queue = deque()

queue.append(start)
visited[start] = 1
vis_num = 1

while queue:
    now = queue.popleft()
    for c in graphs[now]:
        if not visited[c]:
            queue.append(c)
            vis_num += 1
            visited[c] = vis_num

for i in range(1, N+1):
    print(visited[i])
