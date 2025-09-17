# 최소 신장 트리
import heapq

def prim(start, V, adj):
    # start: 시작 정점 번호
    # V: 정점 개수
    # adj: 인접리스트

    # 정점을 뽑는다.
    visited = [False] * (V+1)
    # 우선순위 큐
    pq = []

    # 첫번째 정점을 그냥 큐에 넣는다.
    heapq.heappush(pq, (0, start)) # (가중치, 노드)
    # 기본적으로 모든 노드까지의 가중치는 무한대이다.

    total_weight = 0
    cnt = 0 # 선택된 정점 수

    while pq:
        w, node = heapq.heappop(pq) # 최소 가중치의 정점 선택

        # heapq에서 가장 작은 것을 뽑았을 때, 해당 정점이 트리에 포함된다.
        if visited[node]:
            continue
        # 뽑고나서 visited 처리
        visited[node] = True
        total_weight += w
        cnt += 1
        # 트리에 정점이 하나 추가된다.
        # 현재 형성된 트리를 기준으로 하여
        # 만약 모든 정점을 다 선택 완료 했다면!
        if cnt == V+1:
            break

        # 현재 선택된 정점의 인접노드의 가중치 업데이트를 한 후 큐에 집어 넣는다.
        for next_w, next_node in adj[node]: # 모든 이웃 정점 중에서
            if not visited[next_node]:
                heapq.heappush(pq, (next_w, next_node))

    return total_weight

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((w, n2))
        adj[n2].append((w, n1))

    result = prim(0, V, adj)

    print(f"#{t}", result)