T = int(input())

for test_case in range(1, T + 1):

    # 12712. 파리퇴치3
    N, M = map(int, input().split())
    flies = [[int(x) for x in input().split()] for _ in range(N)]

    # 최대 파리 수
    max_flies = 0
    cross, plus = [], []
    for i in range(1, M):
        cross.extend([(-i, -i), (-i, i), (i, -i), (i, i)])
        plus.extend([(i, 0), (-i, 0), (0, i), (0, -i)])
    
    for i in range(N):
        for j in range(N):
            # + 모양
            plus_flies, cross_flies = 0, 0
            for p in plus:
                if (0 <= i + p[0] < N) and (0 <= j + p[1] < N):
                    plus_flies += flies[i + p[0]][j + p[1]]
            # x 모양
            for c in cross:
                if (0 <= i + c[0] < N) and (0 <= j + c[1] < N):
                    cross_flies += flies[i + c[0]][j + c[1]]
            if cross_flies >= plus_flies:
                max_flies = max(max_flies, cross_flies+flies[i][j])
            else:
                max_flies = max(max_flies, plus_flies+flies[i][j])

    print(f'#{test_case} {max_flies}')