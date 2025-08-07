# 파리퇴치3

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    flies = [[int(x) for x in input().split()] for _ in range(N)]

    plus_attack_range = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    cross_attack_range = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    max_flies = 0

    for i in range(N):
        for j in range(N):
            plus_sum, cross_sum = 0, 0

            # 중앙 칸의 파리 퇴치
            plus_sum += flies[i][j]
            cross_sum += flies[i][j]

            # +, x 영역으로 각각 파리 퇴치
            for p in plus_attack_range:
                for m in range(1, M):
                    next_i, next_j = i + p[0] * m, j + p[1] * m
                    if (0 <= next_i < N) and (0 <= next_j < N):
                        plus_sum += flies[next_i][next_j]
            
            for c in cross_attack_range:
                for m in range(1, M):
                    next_i, next_j = i + c[0] * m, j + c[1] * m
                    if (0 <= next_i < N) and (0 <= next_j < N):
                        cross_sum += flies[next_i][next_j]

            if max_flies < plus_sum:
                max_flies = plus_sum
            if max_flies < cross_sum:
                max_flies = cross_sum
    
    print(f'#{t} {max_flies}')