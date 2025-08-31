# 2589. 보물섬
from collections import deque

R, C = map(int, input().split())

board = [[x for x in input()] for _ in range(R)]

max_length = -1
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    length = -1
    dist = [[-1] * C for _ in range(R)]

    stack = deque()

    dist[i][j] = 0
    stack.append((i, j))

    while stack:
        i, j = stack.popleft()
        length = max(length, dist[i][j])

        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < R and 0 <= nj < C:
                if board[ni][nj] == 'L' and dist[ni][nj] == -1:
                    stack.append((ni, nj))
                    dist[ni][nj] = dist[i][j] + 1  

    return length

for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            max_length = max(max_length, dfs(i, j))

print(max_length)