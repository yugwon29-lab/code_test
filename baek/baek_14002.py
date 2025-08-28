# 14002. 가장 긴 증가하는 부분 수열 4

N = int(input())
A = [int(x) for x in input().split()]

# 테이블 정의
dp = [[1, -1] for _ in range(N)]
# DP[i][0] : i번째 수가 포함된 가장 긴 증가 수열의 길이
# DP[i][1] : i번째 수 다음으로 작은 숫자의 인덱스 정보

# 초기값 정의
dp[0][0] = 1
dp[0][1] = -1

# 점화식
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = j

max_value = 0
max_idx = -1
for i in range(N):
    if dp[i][0] > max_value:
        max_value = dp[i][0]
        max_idx = i

result = []
idx = max_idx
while idx != -1:
    result.append(A[idx])
    idx = dp[idx][1]
result.reverse()
print(max_value)
print(*result)