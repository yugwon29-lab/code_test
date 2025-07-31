from collections import deque

# 4179. 불!

# 입력 받기
R, C = map(int, input().split())
maze = [[c for c in input()] for _ in range(R)]

# 이동 가능 경우의 수
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 거리 배열 (불, 지훈)
fire_dist = [[-1 for _ in range(C)] for _ in range(R)]
jihoon_dist = [[-1 for _ in range(C)] for _ in range(R)]

# 불과 지훈의 시작점 찾기
start_f, start_j = [], None
for r in range(R):
    for c in range(C):
        if maze[r][c] == 'F':
            start_f.append((r,c))
        elif maze[r][c] == 'J':
            start_j = (r, c)

# 불 BFS
queue = deque()

for fr, fc in start_f:
    fire_dist[fr][fc] = 1
    queue.append((fr, fc))

while len(queue) != 0:
    i, j = queue.popleft()

    for m in move:
        next_i, next_j = i + m[0], j + m[1]
        # 미로 밖이거나 벽이면 continue
        if (0 <= next_i < R) and (0 <= next_j < C) and maze[next_i][next_j] != '#':
            if fire_dist[next_i][next_j] == -1:
                fire_dist[next_i][next_j] = fire_dist[i][j] + 1
                queue.append((next_i, next_j))
        else:
            continue

# 지훈 BFS
can_run = False
min_time = float('inf')
queue = deque()

jihoon_dist[start_j[0]][start_j[1]] = 1
queue.append(start_j)

while len(queue) != 0:
    i, j = queue.popleft()
    # 미로의 끝에 도달하면 지훈은 탈출 가능한 상태이다.
    # 탈출 가능 상태로 바꾸고, 그 때 시간이 최소면 업데이트한다.
    if i == 0 or j == 0 or i == R - 1 or j == C - 1:
        can_run = True
        if min_time > jihoon_dist[i][j]:
            min_time = jihoon_dist[i][j]

    for m in move:
        next_i, next_j = i + m[0], j + m[1]
        # 미로 밖이거나 벽이면 continue
        if (0 <= next_i < R) and (0 <= next_j < C) and maze[next_i][next_j] != '#':
            # 불이 이미 퍼졌다면... continue + 불이 지나간 곳이여야 함.
            if fire_dist[next_i][next_j] <= jihoon_dist[i][j] + 1 and fire_dist[next_i][next_j] != -1:
                continue

            # 아니면 지훈이 갈 수 있음
            if jihoon_dist[next_i][next_j] == -1:
                jihoon_dist[next_i][next_j] = jihoon_dist[i][j] + 1
                queue.append((next_i, next_j))
        else:
            continue

if can_run:
    # 마지막 공간에서 탈출까지 걸리는 시간까지 더해줘야 한다.
    print(min_time)
else:
    print('IMPOSSIBLE')