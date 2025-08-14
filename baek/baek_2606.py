# 2606. 바이러스
from collections import deque

N = int(input())
E = int(input())

# 그래프
graphs = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(E):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

start = 1
queue = deque()

queue.append(start)
visited[start] = True
cnt = 0

while queue:
    now = queue.popleft()
    for c in graphs[now]:
        if not visited[c]:
            queue.append(c)
            visited[c] = True
            cnt += 1

print(cnt)
