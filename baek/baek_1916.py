# 1916. 최소비용 구하기
from heapq import heappop, heappush

N = int(input())
M = int(input())
graphs = [[] for _ in range(N+1)]

INF = float('inf')

for _ in range(M):
    s, e, t = map(int, input().split())
    graphs[s].append((t, e))

def dijkstra(st):
    pq = []
    dist_arr = [INF] * (N+1)

    heappush(pq, (0, st))
    dist_arr[st] = 0

    while pq:
        dist, node = heappop(pq)

        if dist_arr[node] != dist:
            continue

        for nxt_dist, nxt_node in graphs[node]:
            new_dist = dist + nxt_dist

            if dist_arr[nxt_node] <= new_dist:
                continue

            dist_arr[nxt_node] = new_dist
            heappush(pq, (new_dist, nxt_node))

    return dist_arr

S, E = map(int, input().split())
result = dijkstra(S)

print(result[E])