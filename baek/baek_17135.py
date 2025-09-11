# 17135. 캐슬 디펜스
from collections import deque
from itertools import combinations

N, M, D = map(int, input().split())
castle = [[int(x) for x in input().split()] for _ in range(N)]

move = [(-1, 0), (0, 1), (0, -1)]

# 궁수의 타겟
def target(j, cut):
    min_j = M
    min_range = D+1
    dist = [[-1] * M for _ in range(N)]

    i, j = N, j
    queue = deque()
    queue.append((i, j))

    ti, tj = None, None

    while queue:
        i, j = queue.popleft()
        if i < N:
            if castle[i][j] == 1 and not cut[i][j]:
                if min_range >= dist[i][j] and dist[i][j] <= D:
                    min_range = dist[i][j]
                    if min_j >= j:
                        ti, tj = i, j
                        min_j = j

            if min_range < dist[i][j]:
                break

        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < N and 0 <= nj < M:
                if dist[ni][nj] == -1:
                    if i == N:
                        dist[ni][nj] = 1
                    else:
                        dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))
    
    return ti, tj

max_enemy = 0
tmp = N
for shot in combinations(range(M), 3):
    N = tmp
    enemy = 0
    cut = [[False] * M for _ in range(N)]
    while N >= 0:
        targets = []
        for s in shot:
            ti, tj = target(s, cut)
            if ti is not None:
                targets.append((ti, tj))
        for ti, tj in targets:
            if not cut[ti][tj]:
                enemy += 1
                cut[ti][tj] = True
        N -= 1
    if max_enemy < enemy:
        max_enemy = enemy

print(max_enemy)
