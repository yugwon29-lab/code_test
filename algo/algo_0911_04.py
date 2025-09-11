# 정사각형 방
T = int(input())

for t in range(1, T+1):
    N = int(input())
    A = [[int(x) for x in input().split()] for _ in range(N)]

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # DP[i][j] 이 칸에서는 최대 0칸만큼 갈 수 있음
    DP = [[-1] * N for _ in range(N)]

    def found(i, j):
        if DP[i][j] != -1:
            return DP[i][j]
        cnt = 1
        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < N and 0 <= nj < N:
                if A[ni][nj] == A[i][j] + 1:
                    cnt += found(ni, nj)
        DP[i][j] = cnt
        return cnt
    
    max_box = 0
    min_value = N * N + 1
    for i in range(N):
        for j in range(N):
            if max_box == found(i, j):
                if min_value > A[i][j]:
                    min_value = A[i][j]
            elif max_box < DP[i][j]:
                max_box = DP[i][j]
                min_value = A[i][j]

    print(f'#{t}', min_value, max_box)