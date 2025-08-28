# 1937. 욕심쟁이 판다
import sys

sys.setrecursionlimit(1000000)

N = int(input())
shoop = [[int(x) for x in input().split()] for _ in range(N)]

dp = [[0] * N for _ in range(N)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    if dp[i][j] != 0:
        return dp[i][j]
    
    dp[i][j] = 1

    for m in move:
        ni, nj = i + m[0], j + m[1]
        if 0 <= ni < N and 0 <= nj < N:
            if shoop[ni][nj] > shoop[i][j]:
                dp[i][j] = max(dp[i][j], dfs(ni, nj) + 1)

    return dp[i][j]

max_value = 0
for i in range(N):
    for j in range(N):
        value = dfs(i, j)
        if max_value < value:
            max_value = value

print(max_value)

    