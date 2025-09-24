# 5719. 거의 최단 경로
from heapq import heappush, heappop

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())

    graphs = [[] for _ in range(N)]
    for _ in range(M):
        u, v, p = map(int, input().split())
        graphs[u].append((p, v))

    INF = float('inf')

    def dijkstra(st):
        pq = []
        dist_arr = [INF] * N
        pre_node = [[] for _ in range(N)]

        heappush(pq, (0, st))
        dist_arr[st] = 0

        while pq:
            dist, node = heappop(pq)

            if dist_arr[node] != dist:
                continue

            for nxt_dist, nxt_node in graphs[node]:
                new_dist = dist + nxt_dist

                if dist_arr[nxt_node] < new_dist:
                    continue
                
                if dist_arr[nxt_node] > new_dist:
                    dist_arr[nxt_node] = new_dist
                    heappush(pq, (new_dist, nxt_node))
                    pre_node[nxt_node] = [node]
                elif dist_arr[nxt_node] == new_dist:
                    pre_node[nxt_node].append(node)

        return dist_arr, pre_node
    
    def remove_edges(r_node, dest):
        q = [dest]
        visited = [False] * N
        while q:
            cur = q.pop()
            if visited[cur]:
                continue
            visited[cur] = True
            for prev in r_node[cur]:
                # prev → cur 간선 제거
                graphs[prev] = [(w, nxt) for (w, nxt) in graphs[prev] if nxt != cur]
                q.append(prev)
    
    r_dist, r_node = dijkstra(S)
    remove_edges(r_node, D)
    result, _ = dijkstra(S)

    print(result[D] if result[D] != INF else -1)
