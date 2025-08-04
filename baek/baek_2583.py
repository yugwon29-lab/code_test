from collections import deque

# 2583. 영역 구하기

M, N, K = map(int, input().split())
grid = [[0 for _ in range(N)] for _ in range(M)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 직사각형 입력
for k in range(K):
    min_x, min_y, max_x, max_y = map(int, input().split())
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            grid[y][x] = 1

# BFS
visited = [[-1 for _ in range(N)] for _ in range(M)]
area_list = []

for y in range(M):
    for x in range(N):
        if grid[y][x] == 0 and visited[y][x] == -1:
            start_y, start_x = y, x
            visited[start_y][start_x] = 0
            area = 0

            queue = deque()
            queue.append((start_y, start_x))

            while queue:
                now_y, now_x = queue.popleft()
                area += 1

                for m in move:
                    next_y, next_x = now_y + m[0], now_x + m[1]

                    if (0 <= next_y < M) and (0 <= next_x < N):
                        if grid[next_y][next_x] == 0 and visited[next_y][next_x] == -1:
                            visited[next_y][next_x] = 0
                            queue.append((next_y, next_x))

            area_list.append(area)

print(len(area_list))
area_list.sort()
for a in area_list:
    print(a, end=" ")
print()
