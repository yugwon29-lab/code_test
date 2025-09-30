# 1497. 기타콘서트
N, M = map(int, input().split())

guitar = [0] * N

for n in range(N):
    name, able = input()
    S = 0
    for m in range(M):
        if able[m] == 'Y':
            S = S | (1 << (m))

used = [False] * N
def dfs(cur, )