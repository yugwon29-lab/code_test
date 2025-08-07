# 달팽이 숫자

T = int(input())

for t in range(1, T+1):
    N = int(input())

    now_i, now_j = 0, -1
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    m = 0
    num = 1
    crit = N

    array = [[0] * N for _ in range(N)]

    while crit != 0:
        if crit == N:
            for i in range(crit):
                now_i, now_j = now_i + move[m][0], now_j + move[m][1]
                array[now_i][now_j] = num
                num += 1
            m = (m + 1) % 4
        else:
            for i in range(2):
                for j in range(crit):
                    now_i, now_j = now_i + move[m][0], now_j + move[m][1]
                    array[now_i][now_j] = num
                    num += 1
                m = (m + 1) % 4
        crit -= 1
    
    print(f'#{t}')
    for i in range(N):
        print(*array[i])