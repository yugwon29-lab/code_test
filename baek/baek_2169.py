# 2169. 로봇 조종하기
from collections import deque

N, M = map(int, input().split())
mars = [[int(x) for x in input().split()] for _ in range(N)]

# 점화식 정의
# DP[i][j] = i행 j열에 도달했을 때, 탐사 가치의 최댓값
DP = [[0] * M for _ in range(N)]

# 초기값 설정
for j in range(M):
    if j == 0:
        DP[0][j] = mars[0][j]
    else:
        DP[0][j] = DP[0][j-1] + mars[0][j]

# 움직이는 방향
for i in range(1, N):
    left = [0] * M
    right = [0] * M

    # 왼쪽에서 오른쪽
    left[0] = DP[i-1][0] + mars[i][0]
    for j in range(1, M):
        left[j] = max(left[j-1], DP[i-1][j]) + mars[i][j]

    # 오른쪽에서 왼쪽
    right[M-1] = DP[i-1][M-1] + mars[i][M-1]
    for j in range(M-2, -1, -1):
        right[j] = max(right[j+1], DP[i-1][j]) + mars[i][j]

    # 최종 DP 값
    for j in range(M):
        DP[i][j] = max(left[j], right[j])

print(DP[N-1][M-1])
