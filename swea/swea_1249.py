# 1249. 보급로
from collections import deque

T = int(input())

for t in range(1, T+1):
    N = int(input())
    road = [[int(x) for x in input()] for _ in range(N)]

    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dist = [[-1] * N for _ in range(N)]
    
    # 출발점 설정
    si, sj = 0, 0
    queue = deque()

    dist[si][sj] = 0
    queue.append((si, sj))
    while queue:
        i, j = queue.popleft()

        for m in move:
            ni, nj = i + m[0], j + m[1]
            if (0 <= ni < N) and (0 <= nj < N):
                if dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + road[ni][nj]
                    queue.append((ni, nj))
                elif dist[ni][nj] > dist[i][j] + road[ni][nj]:
                    dist[ni][nj] = dist[i][j] + road[ni][nj]
                    queue.append((ni, nj))

    print(f'#{t} {dist[N-1][N-1]}')