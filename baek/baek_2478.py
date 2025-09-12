# 2478. 자물쇠
N = 10
A = [int(x) for x in input().split()]

# 마지막 K 왼쪽밀기 횟수
a, b = 0, N-1
k2 = 0
while A[a] == A[b] + 1 or A[a] == A[b] - 1:
    k2 += 1
    a -= 1
    b -= 1
A = A[b:] + A[:b]

# 반전 구간 찾기
idx = 0
increasing = True
while increasing:
    if idx
