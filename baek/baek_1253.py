# 1253. 좋다
N = int(input())
A = [int(x) for x in input().split()]

A.sort()

cnt = 0

c = 0
while c < N:
    a, b = 0, N-1
    while a < b:
        if a == c:
            a += 1
            continue
        if b == c:
            b -= 1
            continue
        total = A[a] + A[b]
        if A[c] > total:
            a += 1
        elif A[c] < total:
            b -= 1
        else:
            cnt += 1
            break
    c += 1

print(cnt)
