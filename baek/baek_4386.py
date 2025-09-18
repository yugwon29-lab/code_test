# 4386. 별자리 만들기
import math
import heapq

def prim(start, N, adj):
    visited = [False] * N
    pq = []

    heapq.heappush(pq, (0, start))

    total_cost = 0
    cnt = 0

    while pq:
        cost, star = heapq.heappop(pq)

        if visited[star]:
            continue
        
        visited[star] = True
        total_cost += cost
        cnt += 1

        if cnt == N:
            break

        for next_cost, next_star in adj[star]:
            if not visited[next_star]:
                heapq.heappush(pq, (next_cost, next_star))
        
    return total_cost

N = int(input())
x = []
y = []

adj = [[] for _ in range(N)]

for _ in range(N):
    ix, iy = map(float, input().split())
    x.append(ix)
    y.append(iy)

for i in range(N):
    for j in range(i+1, N):
        dx = abs(x[i] - x[j])
        dy = abs(y[i] - y[j])
        dist = math.sqrt((dx * dx) + (dy * dy))
        adj[i].append((dist, j))
        adj[j].append((dist, i))

result = prim(0, N, adj)
print(f'{result:.2f}')