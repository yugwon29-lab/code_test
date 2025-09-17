# 1647. 도시 분할 계획
import heapq

def prim(start, N, adj):
    pq = []
    visited = [False] * (N+1)

    heapq.heappush(pq, (0, start))

    total_cost = 0
    cnt = 0
    max_cost = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        max_cost = max(max_cost, cost)
        total_cost += cost
        cnt += 1

        if cnt == N:
            break

        for next_c, next_node in adj[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_c, next_node))

    return total_cost - max_cost


N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graphs[a].append((c, b))
    graphs[b].append((c, a))

result = prim(1, N, graphs)

print(result)
