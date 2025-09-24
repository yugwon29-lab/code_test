# 1753. 최단 경로
import heapq

INF = float('inf')
V, E = map(int, input().split())
K = int(input())
graphs = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graphs[u].append((w, v))

def dijkstra(start_node):
    pq = []
    
    # 시작 노드를 넣어준다.
    heapq.heappush(pq, (0, start_node))

    # 시작 노드에서 다른 모든 정점까지의 거리를 우선 무한대로 설정
    dists = [INF] * (V+1)

    # 시작 노드까지의 거리는 0으로 설정
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] != dist:
            continue

        for nxt_dist, nxt_node in graphs[node]:
            new_dist = dist + nxt_dist

            if dists[nxt_node] <= new_dist:
                continue

            dists[nxt_node] = new_dist
            heapq.heappush(pq, (new_dist, nxt_node))

    return dists

result = dijkstra(K)

for i in range(1, V+1):
    if i == K:
        print(0)
    elif result[i] == INF:
        print('INF')
    else:
        print(result[i])