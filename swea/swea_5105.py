T = int(input())

for test_case in range(1, T + 1):

    # 5105. 미로의 거리
    N = int(input())
    board = [[int(x) for x in input()] for y in range(N)]

    # 방문 기록
    visited = [[False for x in range(N)] for y in range(N)]

    # 상, 하, 좌, 우 움직임 튜플
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))

    # start, end 지점 생성
    # 벽은 방문 처리
    start, end = None, None
    num = 0
    find_route = False
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start = (i, j)
            elif board[i][j] == 3:
                end = (i, j)
            elif board[i][j] == 1:
                visited[i][j] = True

    # queue 생성
    queue = []
    n = 0   # 깊이 알리미
    v = start  # 시작점
    queue.append(v)
    n += 1
    while queue:
        # print(num, len(queue))
        t = queue.pop(0)
        n -= 1
        if not visited[t[0]][t[1]]:
            visited[t[0]][t[1]] = True
        for m in move:
            next_i, next_j = t[0]+m[0], t[1]+m[1]
            if not (0 <= next_i < N) or not (0 <= next_j < N):
                # 맵 밖으로 나갈 수 없다.
                continue
            else:
                if not visited[next_i][next_j]:
                    queue.append((next_i, next_j))

        if t == end:
            find_route = True
            break

        if n == 0:
            # 깊이 추가
            n += len(queue)
            num += 1

    if not find_route:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {num-1}')
        # 출발점과 도착점의 깊이는 제외


