# 2637. 장난감 조립
from collections import deque

N = int(input())
M = int(input())

deg = [0] * (N+1)
adj = [[] for _ in range(N+1)]
total = [0] * (N+1)
total[N] = 1
used = [False] * (N+1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    adj[X].append((Y, K))
    deg[Y] += 1
    if not used[X]:
        used[X] = True

q = deque()
q.append(N)

while q:
    now = q.popleft()
    for nxt, cnt in adj[now]:
        deg[nxt] -= 1
        total[nxt] += cnt * total[now] if now != N else cnt
        if deg[nxt] == 0:
            q.append(nxt)

for i in range(1, N+1):
    if not used[i]:
        print(i, total[i])