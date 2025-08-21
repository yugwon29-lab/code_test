# 1149. RGB거리

# 입력 받기
N = int(input())
cost = [(0, 0, 0)]
for i in range(N):
    r, g, b = map(int, input().split())
    cost.append((r, g, b))

# 테이블 설정
d = [[0, 0, 0] for _ in range(N+1)]
# D[i][0,1,2] i번째 집을 R,G,B로 칠했을 때 비용(누적)

# 초기값 설정
d[1][0], d[1][1], d[1][2] = cost[1]

# DP
for i in range(2, N+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + cost[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + cost[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + cost[i][2]

print(min(d[N][0], d[N][1], d[N][2]))