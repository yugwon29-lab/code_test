# 1026. 보물

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort(reverse=True)
B.sort()

total = 0
for i in range(N):
    total += A[i] * B[i]

print(total)
