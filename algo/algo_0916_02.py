# 하나로
# 프림으로 풀어보았다.
import heapq

def prim(start, N, adj):

    visited = [False] * N
    pq = []

    heapq.heappush(pq, (0, start))

    total_weight = 0
    cnt = 0

    while pq:
        w, node = heapq.heappop(pq)

        if visited[node]:
            continue
        visited[node] = True
        total_weight += w
        cnt += 1

        if cnt == N:
            break

        for next_w, next_node in adj[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_w, next_node))

    return total_weight

T = int(input())

for t in range(1, T+1):
    N = int(input())
    idx = [int(x) for x in input().split()]
    idy = [int(y) for y in input().split()]
    E = float(input())

    adj = [[] for _ in range(N)]

    for i in range(N):
        for j in range(i, N):
            dx = idx[i] - idx[j]
            dy = idy[i] - idy[j]
            cost = E * ((dx * dx) + (dy * dy))
            adj[i].append((cost, j))
            adj[j].append((cost, i))

    result = prim(0, N, adj)

    print(f'#{t}', round(result))
