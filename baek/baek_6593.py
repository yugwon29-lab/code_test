from collections import deque

# 6593. 상범빌딩

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []

    for l in range(L):
        layer = [[x for x in input()] for _ in range(R)]
        building.append(layer)
        _ = input()

    # 이동 가능한 경우의 수
    move = [
        (-1, 0, 0),
        (1, 0, 0),
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
    ]  # 상, 하, 동, 서, 남, 북

    # 거리 배열
    dist = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    start, end = None, None

    for z in range(L):
        for y in range(R):
            for x in range(C):
                if building[z][y][x] == "S":
                    start = (z, y, x)
                if building[z][y][x] == "E":
                    end = (z, y, x)

    # BFS
    # 시작점 설정
    queue = deque()

    dist[start[0]][start[1]][start[2]] = 0
    queue.append(start)

    while len(queue) != 0:
        now_z, now_y, now_x = queue.popleft()
        for m in move:
            next_z, next_y, next_x = now_z + m[0], now_y + m[1], now_x + m[2]
            if not (0 <= next_z < L and 0 <= next_y < R and 0 <= next_x < C):
                continue
            else:
                if (
                    building[next_z][next_y][next_x] != "#"
                    and dist[next_z][next_y][next_x] == -1
                ):
                    dist[next_z][next_y][next_x] = dist[now_z][now_y][now_x] + 1
                    queue.append((next_z, next_y, next_x))

    if dist[end[0]][end[1]][end[2]] == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {dist[end[0]][end[1]][end[2]]} minute(s).")
