# 11659. 구간 합 구하기 4

N, M = map(int, input().split())
number = [int(x) for x in input().split()]

# 테이블 설정
d = [0] * (N+1)
# D[i] = i번째 수까지의 합

# 초기값 설정
d[0] = 0

for i in range(1, N+1):
    d[i] = d[i-1] + number[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(d[j]-d[i-1])