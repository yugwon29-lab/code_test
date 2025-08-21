# 미로의 거리
from collections import deque

T = int(input())

for t in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                gi, gj = i, j
                continue
            if maze[i][j] == 2:
                si, sj = i, j
                continue
    
    dist = [[-1] * N for _ in range(N)]
    queue = deque()

    # 시작 지점 설정
    dist[si][sj] = 0
    queue.append((si, sj))

    while queue:
        i, j = queue.popleft()
        if (i, j) == (gi, gj):
            break

        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] != 1 and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    queue.append((ni, nj))

    if dist[gi][gj] != -1:
        print(f'#{t} {dist[gi][gj]-1}')
    else:
        print(f'#{t} 0')