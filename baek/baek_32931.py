# 32931. 자석 놀이
N = int(input())
cards = [[int(x) for x in input().split()] for _ in range(2)]

DP = [[0] * N for _ in range(2)]

# 초기값 설정
DP[0][0] = max(cards[0][0] + cards[1][0], cards[0][0])
DP[1][0] = cards[0][0] + cards[1][0]

for i in range(1, N):
    DP[0][i] = max(DP[0][i-1] + max(cards[0][i] + cards[1][i], cards[0][i]), DP[1][i-1] + cards[0][i] + cards[1][i])
    DP[1][i] = max(DP[0][i-1] + cards[0][i] + cards[1][i], DP[1][i-1] + max(cards[0][i] + cards[1][i], cards[1][i]))

print(DP[1][N-1])