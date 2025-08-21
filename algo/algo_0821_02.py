# 노드의 거리
from collections import deque

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    graphs = [[] for _ in range(V+1)]

    for e in range(E):
        a, b = map(int, input().split())
        graphs[a].append(b)
        graphs[b].append(a)

    S, G = map(int, input().split())

    dist = [-1] * (V+1)
    queue = deque()

    queue.append(S)
    dist[S] = 0

    while queue:
        now = queue.popleft()
        if now == G:
            break
        for g in graphs[now]:
            if dist[g] == -1:
                dist[g] = dist[now] + 1
                queue.append(g)
    
    if dist[G] == -1:
        print(f'#{t} 0')
    else:
        print(f'#{t} {dist[G]}')



