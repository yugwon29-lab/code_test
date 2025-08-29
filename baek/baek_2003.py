# 2003. 수들의 합 2
N, M = map(int, input().split())

A = [int(x) for x in input().split()]

cnt = 0
st, en = 0, 0
total = A[st]
while True:
    if total <= M:
        if total == M:
            cnt += 1
        en += 1
        if en >= N:
            break
        total += A[en]
    else:
        if st != en:
            total -= A[st]
            st += 1
        else:
            st += 1
            en += 1
            if en >= N:
                break
            total = A[st]

print(cnt)