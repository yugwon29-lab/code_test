# 11437. LCA
from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parents = [-1] * (N+1)
depth = [0] * (N+1)

def bfs(root):
    q = deque()
    q.append(root)

    while q:
        now = q.popleft()

        for nxt in adj[now]:
            if nxt == parents[now]:
                continue
            q.append(nxt)
            parents[nxt] = now
            depth[nxt] = depth[now] + 1

bfs(1)

def find_parents(a, b):
    # 깊이 맞추기
    while depth[a] > depth[b]:
        a = parents[a]
    while depth[a] < depth[b]:
        b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]

    return a
        
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    result = find_parents(a, b)
    print(result)

