# 10844. 쉬운 계단 수

N = int(input())

D = [[0] * (10) for _ in range(N+1)]

# 계단 수의 정의
for i in range(1, 10):
    D[1][i] = 1

for j in range(2, N+1):
    for i in range(10):
        if i == 0:
            D[j][i] = D[j-1][i+1]
        elif i == 9:
            D[j][i] = D[j-1][i-1]
        else:
            D[j][i] = D[j-1][i+1] + D[j-1][i-1]

total = 0
for i in range(0, 10):
    total += D[N][i]

print(total % 1000000000)