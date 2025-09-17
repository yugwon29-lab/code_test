# 하나로
# 크루스칼으로 풀어보았다
import heapq


def find(a):
    global parents
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    aRoot = find(a)
    bRoot = find(b)

    parents[bRoot] = aRoot


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    idx = [int(x) for x in input().split()]
    idy = [int(y) for y in input().split()]
    E = float(input())

    edges = []

    for i in range(N):
        for j in range(i, N):
            dx = idx[i] - idx[j]
            dy = idy[i] - idy[j]
            cost = E * ((dx * dx) + (dy * dy))
            heapq.heappush(edges, (cost, i, j))

    parents = [0] * N
    for i in range(N):
        parents[i] = i

    dist = 0
    cnt = 0

    while True:
        c, i, j = heapq.heappop(edges)

        if find(i) != find(j):
            union(i, j)
            dist += c
            cnt += 1

        if cnt == N-1:
            break

    print(f'#{t}', round(dist))
