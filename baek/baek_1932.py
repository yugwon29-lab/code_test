# 1932. 정수 삼각형
N = int(input())
tri = [[int(x) for x in input().split()] for _ in range(N)]

# 테이블 정의
DP = []
for i in range(1, N+1):
    DP.append([0] * i)
# DP[i][j] = 이 지점까지 갔을 때 얻을 수 있는 정수의 합 최댓값

# 초기값 설정
DP[0][0] = tri[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j - 1 >= 0:
            DP[i][j] = max(DP[i][j], DP[i-1][j-1] + tri[i][j])
        if j <= i-1:
            DP[i][j] = max(DP[i][j], DP[i-1][j] + tri[i][j])

max_value = 0
for i in range(N):
    max_value = max(max_value, DP[N-1][i])

print(max_value)
