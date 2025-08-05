from collections import deque

T = int(input())

for test_case in range(1, T + 1):

    # 1953. 탈주범 검거
    N, M, R, C, L = map(int, input().split())
    jiha_map = [[int(x) for x in input().split()] for _ in range(N)]

    # 움직일 수 있는 경우
    move_dict = {
        1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (0, 1)],
        4: [(-1, 0), (0, 1)],
        5: [(1, 0), (0, 1)],
        6: [(1, 0), (0, -1)],
        7: [(-1, 0), (0, -1)]
    }

    # 이동 가능 터널
    connect_dict = {
        (-1, 0): [1, 2, 5, 6],
        (1, 0): [1, 2, 4, 7],
        (0, -1): [1, 3, 4, 5],
        (0, 1): [1, 3, 6, 7]
    }

    time_map = [[-1] * M for _ in range(N)]

    # 시작점 설정
    st_i, st_j = R, C
    queue = deque()

    time_map[st_i][st_j] = 1
    queue.append((st_i, st_j))

    while queue:
        now_i, now_j = queue.popleft()
        if time_map[now_i][now_j] == L:
            break

        for m in move_dict[jiha_map[now_i][now_j]]:
            next_i, next_j = now_i + m[0], now_j + m[1]
            if (0 <= next_i < N) and (0 <= next_j < M):
                if jiha_map[next_i][next_j] in connect_dict[m] and jiha_map[next_i][next_j] != 0 and time_map[next_i][next_j] == -1:
                    time_map[next_i][next_j] = time_map[now_i][now_j] + 1
                    queue.append((next_i, next_j))
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 1 <= time_map[i][j] <= L:
                cnt += 1

    print(f'#{test_case} {cnt}')