# 9461. 파도반 수열

T = int(input())

d = [0] * 101

d[1], d[2], d[3], d[4], d[5] = 1, 1, 1, 2, 2
for i in range(6, 101):
    d[i] = d[i-5] + d[i-1]

for t in range(1, T+1):
    N = int(input())
    print(d[N])