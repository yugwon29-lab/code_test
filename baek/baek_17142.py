# 17142. 연구소 3
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
lab = [[int(x) for x in input().split()] for _ in range(N)]

dist = [[-1] * N for _ in range(N)]

virus = []
remain = N * N
for i in range(N):
    for j in range(N):
        if lab[i][j] == 1:
            dist[i][j] = "-"
            remain -= 1
        if lab[i][j] == 2:
            dist[i][j] = "*"
            remain -= 1
            virus.append((i, j))


min_time = -1

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for comb in combinations(virus, M):
    can_virus = False
    rem = remain
    max_time = 0
    now_dist = [row[:] for row in dist]
    queue = deque()
    for y, x in comb:
        now_dist[y][x] = 0
        queue.append((y, x))
    
    while queue:
        i, j = queue.popleft()

        if rem == 0:
            can_virus = True
            break

        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < N and 0 <= nj < N:
                if now_dist[ni][nj] == -1:
                    now_dist[ni][nj] = now_dist[i][j] + 1
                    rem -= 1
                    queue.append((ni, nj))
                    if now_dist[ni][nj] > max_time:
                        max_time = now_dist[ni][nj]
                elif now_dist[ni][nj] == "*":
                    now_dist[ni][nj] = now_dist[i][j] + 1
                    queue.append((ni, nj))
                    if now_dist[ni][nj] > max_time:
                        max_time = now_dist[ni][nj]
    
    if can_virus:
        min_time = min(max_time, min_time) if min_time != -1 else max_time

print(min_time)