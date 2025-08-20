# 16173. 점프왕 쩰리 (Small)
from collections import deque

N = int(input())
board = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[False] * N for _ in range(N)]

move = [(1, 0), (0, 1)]

# 시작점 설정
queue = deque()

i, j = 0, 0
visited[i][j] = True

queue.append((i, j))

while queue:
    i, j = queue.popleft()

    if board[i][j] == -1:
        break

    for m in move:
        ni, nj = i + m[0] * board[i][j], j + m[1] * board[i][j]
        if 0 <= ni < N and 0 <= nj < N:
            if not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append((ni, nj))

if visited[N-1][N-1]:
    print('HaruHaru')
else:
    print('Hing')