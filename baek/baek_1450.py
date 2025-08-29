# 1450. 냅색문제

N, C = map(int, input().split())
weight = [int(x) for x in input().split()]

def subset_sums(arr):
    sums = [0]
    for x in arr:
        nxt = []
        for s in sums:
            t = s + x
            if t <= C:
                nxt.append(t)
        sums += nxt
    return sums

left, right = weight[:N//2], weight[N//2:]

A = subset_sums(left)
B = subset_sums(right)

A.sort()
B.sort(reverse=True)

cnt = 0
a, b = 0, 0
while a < len(A) and b < len(B):
    if A[a] + B[b] <= C:
        cnt += len(B) - b
        a += 1
    else:
        b += 1

print(cnt)