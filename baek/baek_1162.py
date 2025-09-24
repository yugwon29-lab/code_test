# 1162. 도로포장
from heapq import heappush, heappop

N, M, K = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graphs[s].append((t, e))
    graphs[e].append((t, s))

INF = float('inf')

def dijkstra(st):
    pq = []
    dist_arr = [[INF] * (K+1) for _ in range(N+1)]

    heappush(pq, (0, st, 0))
    dist_arr[st][0] = 0

    while pq:
        dist, node, wrap = heappop(pq)

        if dist_arr[node][wrap] != dist:
            continue

        for nxt_dist, nxt_node in graphs[node]:
            new_dist = dist + nxt_dist

            if dist_arr[nxt_node][wrap] > new_dist:
                dist_arr[nxt_node][wrap] = new_dist
                heappush(pq, (new_dist, nxt_node, wrap))

            if wrap < K and dist_arr[nxt_node][wrap+1] > dist:
                dist_arr[nxt_node][wrap+1] = dist
                heappush(pq, (dist, nxt_node, wrap+1))

    return dist_arr

result = dijkstra(1)

print(min(result[N]))