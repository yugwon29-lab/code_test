# 16398. 행성 연결
import heapq

N = int(input())
flow = [[int(x) for x in input().split()] for _ in range(N)]

edges = []
for i in range(N):
    for j in range(i, N):
        heapq.heappush(edges, (flow[i][j], i, j))

parents = [i for i in range(N)]

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

cost = 0
cnt = 0

while True:
    c, i, j = heapq.heappop(edges)

    if find(i) != find(j):
        union(i, j)
        cost += c
        cnt += 1

    if cnt == N-1:
        break

print(cost)
