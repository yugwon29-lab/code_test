# 2230. 수 고르기
N, M = map(int, input().split())

A = []

for i in range(N):
    A.append(int(input()))

A.sort()

min_diff = None

st, en = 0, 0

while en < N and st <= en:
    now_diff = A[en] - A[st]
    if now_diff >= M:
        min_diff = now_diff if min_diff is None or min_diff > now_diff else min_diff
        st += 1
    else:
        en += 1

print(min_diff)