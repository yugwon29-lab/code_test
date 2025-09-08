# 탈주범 검거 (2회차)
from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]

    # 터널 정보(이 터널에서 움직일 수 있는 방향)
    tunnel_go = {
        1: [(1, 0), (-1, 0), (0, 1), (0, -1)],
        2: [(1, 0), (-1, 0)],
        3: [(0, 1), (0, -1)],
        4: [(-1, 0), (0, 1)],
        5: [(1, 0), (0, 1)],
        6: [(1, 0), (0, -1)],
        7: [(-1, 0), (0, -1)]
    }
    # 터널 정보(다른 터널에서 올 수 있는 방향)
    tunnel_come = {
        1: [(1, 0), (-1, 0), (0, 1), (0, -1)],
        2: [(1, 0), (-1, 0)],
        3: [(0, 1), (0, -1)],
        4: [(1, 0), (0, -1)],
        5: [(-1, 0), (0, -1)],
        6: [(-1, 0), (0, 1)],
        7: [(1, 0), (0, 1)]
    }

    # 도둑이 시간대별로 있을 수 있는 공간을 표시하는 배열
    # 0: 존재할 수 없음
    # i(i>0): i시간에 도둑이 이 위치에 있을 수 있음
    time = [[0] * M for _ in range(N)]
    queue = deque()

    si, sj = R, C
    time[si][sj] = 1
    queue.append((si, sj))
    
    while queue:
        i, j = queue.popleft()
        # 현 위치의 터널 종류
        tunnel = board[i][j]

        # 현 위치에서 이동하기
        for m in tunnel_go[tunnel]:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < N and 0 <= nj < M:
                # 이동할 수 없는 터널
                if board[ni][nj] == 0 or m not in tunnel_come[board[ni][nj]]:
                    continue
                # 이미 방문한 터널
                if time[ni][nj] != 0:
                    continue
                time[ni][nj] = time[i][j] + 1
                queue.append((ni, nj))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 1 <= time[i][j] <= L:
                cnt += 1
    
    print(f'#{t} {cnt}')

