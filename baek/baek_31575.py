# 31575. 도시와 비트코인

N, M = map(int, input().split())
city = [[int(x) for x in input().split()] for _ in range(M)]

dp = [[False] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if i == 0 and j == 0:
            dp[i][j] = True
            continue
        if city[i][j] == 0:
            dp[i][j] = False
            continue

        first_crit = False
        if 0 <= i-1 < M:
            first_crit = dp[i-1][j]

        second_crit = False
        if 0 <= j-1 < N:
            second_crit = dp[i][j-1]

        if first_crit or second_crit:
            dp[i][j] = True
        else:
            dp[i][j] = False

if dp[M-1][N-1]:
    print("Yes")
else:
    print("No")