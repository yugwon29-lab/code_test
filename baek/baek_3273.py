# 3273. 두 수의 합
N = int(input())
A = [int(x) for x in input().split()]
X = int(input())

A.sort()

st, en = 0, N-1
cnt = 0

while st < en:
    if A[st] + A[en] == X:
        cnt += 1
    if A[st] + A[en] > X:
        en -= 1
    else:
        st += 1

print(cnt)