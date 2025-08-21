# 2579. 계단 오르기

# 입력 받기
N = int(input())

# 계단 입력 1번부터 N번까지
stairs = [0] * (N+1)
for i in range(1, N+1):
    stairs[i] = int(input())

# 점화식 정의
d = [[0, 0, 0] for _ in range(N+1)]
# D[i][j] - i번째 계단을 j번 연속으로 밟았을 때 얻는 점수

# 초기값 설정
# 1번째 계단은 1번 연속으로 밖에 밟을 수 없음
d[1][1] = stairs[1]

for i in range(2, N+1):
    # i번째 계단을 1번 연속 밟음 = 전전계단에서 오셨음
    d[i][1] = max(d[i-2][1], d[i-2][2]) + stairs[i]
    # i번째 계단을 2번 연속 밟음 = 전계단에서 오셨음
    d[i][2] = d[i-1][1] + stairs[i]

print(max(d[N][1], d[N][2]))