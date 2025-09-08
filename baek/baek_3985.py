# 3985.롤 케이크

L = int(input())
N = int(input())

cake = [0] * (L + 1)
expect_max = 0
real_max = 0
expect_idx = -1
real_idx = -1
for i in range(1, N+1):
    P, K = map(int, input().split())
    if K - P + 1 > expect_max:
        expect_idx = i
        expect_max = K - P + 1
    cnt = 0
    for n in range(P, K+1):
        if cake[n] == 0:
            cake[n] = i
            cnt += 1
    if cnt > real_max:
        real_idx = i
        real_max = cnt

print(expect_idx)
print(real_idx)
