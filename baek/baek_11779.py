# 11779. 최소비용 구하기 2
from heapq import heappush, heappop
from collections import deque

N = int(input())
M = int(input())

graphs = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graphs[s].append((t, e))

INF = float('inf')

def dijkstra(st):
    pq = []
    dist_arr = [INF] * (N+1)
    pre_node = [0] * (N+1)

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
            pre_node[nxt_node] = node

    return dist_arr, pre_node

S, E = map(int, input().split())
dist_arr, pre_node = dijkstra(S)

print(dist_arr[E])

road = deque()
road.appendleft(E)
while road[0] != S:
    road.appendleft(pre_node[road[0]])

print(len(road))
print(*road)