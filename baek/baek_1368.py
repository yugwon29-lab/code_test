# 1368. 물대기
import heapq

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)
    parents[bRoot] = aRoot

N = int(input())
shs = [int(input()) for _ in range(N)]
arr = [[int(x) for x in input().split()] for _ in range(N)]

edges = []
for i in range(N):
    for j in range(i, N):
        if i == j:
            heapq.heappush(edges, (shs[i], 0, i+1))
        else:
            heapq.heappush(edges, (arr[i][j], i+1, j+1))

parents = [i for i in range(N+1)]

total_cost = 0
cnt = 0

while True:
    cost, a, b = heapq.heappop(edges)

    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        cnt += 1

    if cnt == N:
        break

print(total_cost)

