# 2178. 미로 탐색

# 입력 받기
N, M = map(int, input().split())
maze = [[int(x) for x in input()] for _ in range(N)]

# 가능한 이동 경우의 수
move = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 아래, 위, 오른쪽, 왼쪽

dist = [[-1 for _ in range(M)] for _ in range(N)] # 거리 배열

# 시작 위치 설정
start = (0, 0)
queue = []

dist[start[0]][start[1]] = 1
queue.append(start)

while len(queue) != 0:
    i, j = queue.pop(0)

    # 이동 가능한 모든 경우의 수 확인
    for m in move:
        # 혹시 미로 범위 밖이면 continue
        next_i, next_j = i + m[0], j + m[1]
        if (0 <= next_i < N) and (0 <= next_j < M):
            # 방문하지 않았고, 막히지 않은 곳이면 queue에 추가 및 거리 측정
            if dist[next_i][next_j] == -1 and maze[next_i][next_j] == 1:
                dist[next_i][next_j] = dist[i][j] + 1
                queue.append((next_i, next_j))
        else:
            continue

print(dist[N-1][M-1])
