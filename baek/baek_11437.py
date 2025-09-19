# 11437. LCA
from collections import deque

N = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parents = [-1] * (N+1)

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

bfs(1)

def find_parents(a, b):
    a_parents = []
    while True:
        a_parents.append(a)
        a = parents[a]
        if a == -1:
            break
    b_parents = []
    while True:
        b_parents.append(b)
        b = parents[b]
        if b == -1:
            break
    min_len = len(a_parents) + len(b_parents) + 1
    min_parents = None
    for a in a_parents:
        if a in b_parents:
            min_len = a_parents.index(a) + b_parents.index(a) + 2
            min_parents = a
            break
    for b in b_parents:
        if b in a_parents:
            length = a_parents.index(b) + b_parents.index(b) + 2
            if min_len > length:
                min_len = length
                min_parents = a
            break
    
    return min_parents
    
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    result = find_parents(a, b)
    print(result)

