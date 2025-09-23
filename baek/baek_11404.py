# 11404. 플로이드
N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]

# 간선 입력 받기
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

D = [[float('inf')] * (N+1) for _ in range(N+1)]

# 자기 자신에게 가는데 걸리는 시간은 0이다.
for i in range(N+1):
    D[i][i] = 0

# 모든 1번에 갈 수 있는 간선에 대해서 기록한다.
for i in range(N+1):
    for j, cost in edges[i]:
        # 가장 비용이 저렴한 노선만 남긴다.
        D[i][j] = min(D[i][j], cost)

# 플로이드 알고리즘
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            D[j][k] = min(D[j][k], D[j][i] + D[i][k])

for i in range(1, N+1):
    for j in range(1, N+1):
        if D[i][j] == float('inf'):
            D[i][j] = 0

for i in range(1, N+1):
    print(*D[i][1:])
