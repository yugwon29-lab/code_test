# 미로1
from collections import deque

for _ in range(10):
    t = int(input())
    maze = [[int(x) for x in input()] for _ in range(16)]

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited = [[False] * 16 for _ in range(16)]
    queue = deque()

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si, sj = i, j
                continue
            if maze[i][j] == 3:
                gi, gj = i, j
                continue
    
    visited[si][sj] = True
    queue.append((si, sj))

    while queue:
        i, j = queue.popleft()
        if (i, j) == (gi, gj):
            break

        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < 16 and 0 <= nj < 16:
                if not visited[ni][nj] and maze[ni][nj] != 1:
                    visited[ni][nj] = True
                    queue.append((ni, nj))

    print(f'#{t} {1 if visited[gi][gj] else 0}')