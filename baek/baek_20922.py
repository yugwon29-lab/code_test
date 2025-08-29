# 20922. 겹치는 건 싫어
N, K = map(int, input().split())
A = [int(x) for x in input().split()]
cnt = [0] * 200001
st, en = 0, 0
cnt[A[st]] += 1

max_len = 0
while True:
    if cnt[A[en]] <= K:
        max_len = max(max_len, en - st + 1)
        en += 1
        if en >= N:
            break
        cnt[A[en]] += 1
    else:
        while cnt[A[en]] > K:
            cnt[A[st]] -= 1
            st += 1
        if st > en:
            break

print(max_len)
