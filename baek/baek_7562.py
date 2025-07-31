from collections import deque

# 7562. 나이트의 이동

T = int(input())

for test_case in range(T):
    L = int(input())

    # 나이트 시작 위치
    SI, SJ = map(int, input().split())
    # 나이트 도착 위치
    GI, GJ = map(int, input().split())

    # 나이트의 이동 가능 경우의 수
    move = [(-1, -2), (-1, 2), (1, -2), (1, 2),
            (-2, -1), (-2, 1), (2, -1), (2, 1)]
    
    # 거리 배열
    dist = [[-1 for _ in range(L)] for _ in range(L)]

    # 시작점 설정
    queue = deque()

    dist[SI][SJ] = 0
    queue.append((SI, SJ))

    while len(queue) != 0:
        i, j = queue.popleft()
        # 이미 도착 지점에 도달했다면, 불필요한 연산 모두 제거
        if (i, j) == (GI, GJ):
            break
        

        for m in move:
            next_i, next_j = i + m[0], j + m[1]

            # 나이트가 갈 수 있는 곳이면,
            if (0 <= next_i < L) and (0 <= next_j < L) and dist[next_i][next_j] == -1:
                # 거리 표시 및 큐에 추가
                dist[next_i][next_j] = dist[i][j] + 1
                queue.append((next_i, next_j))

    print(dist[GI][GJ])