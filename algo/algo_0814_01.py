# 미로
from collections import deque

T = int(input())

for t in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    si, sj = -1, -1
    ei, ej = -1, -1

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
            elif maze[i][j] == 3:
                ei, ej = i, j

    queue = deque()
    
    queue.append((si, sj))
    visited[si][sj] = True

    can_go = False

    while queue:
        i, j = queue.pop()
        
        if maze[i][j] == 3:
            can_go = True
            break

        for m in move:
            ni, nj = i + m[0], j + m[1]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if not visited[ni][nj] and maze[ni][nj] != 1:
                queue.append((ni, nj))
                visited[ni][nj] = True

    print(f'#{t} {1 if can_go else 0}')
