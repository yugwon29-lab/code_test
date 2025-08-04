from collections import deque

# 2468. 안전 영역
N = int(input())
area = [[int(x) for x in input().split()] for _ in range(N)]

# 아무 구역도 잠기지 않았다면, 최대 구역은 1개
max_area = 1

# 이동
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for h in range(1, 100):
    num_area = 0
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if area[y][x] > h and visited[y][x] == -1:
                s_y, s_x = y, x
                queue = deque()

                visited[s_y][s_x] = 0
                queue.append((s_y, s_x))

                while queue:
                    now_y, now_x = queue.popleft()

                    for m in move:
                        next_y, next_x = now_y + m[0], now_x + m[1]
                        if (0 <= next_y < N) and (0 <= next_x < N):
                            if (
                                area[next_y][next_x] > h
                                and visited[next_y][next_x] == -1
                            ):
                                visited[next_y][next_x] = 0
                                queue.append((next_y, next_x))

                num_area += 1

    if num_area > max_area:
        max_area = num_area

print(max_area)
