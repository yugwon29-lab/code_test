# 최소 신장 트리
import heapq

def find(a):
    global parents
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    global parents
    aRoot = find(a)
    bRoot = find(b)
    parents[bRoot] = aRoot

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        heapq.heappush(edges, (w, n1, n2))

    parents = [0] * (V+1)
    for i in range(V+1):
        parents[i] = i
    
    dist = 0
    cnt = 0

    while True:
        w, n1, n2 = heapq.heappop(edges)

        if find(n1) != find(n2): # 사이클이 아닌 경우
            union(n1, n2)
            dist += w
            cnt += 1
        
        if cnt == V:
            break

    print(f"#{t}", dist)