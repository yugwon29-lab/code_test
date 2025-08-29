# 1806. 부분합

N, S = map(int, input().split())
numbers = [int(x) for x in input().split()]

st, en = 0, 0
total = numbers[st]
result = None

while en < N and st <= en:
    if total >= S:
        if result is None or result > en - st + 1:
            result = en - st + 1
        total -= numbers[st]
        st += 1
    else:
        en += 1
        if en >= N:
            break
        total += numbers[en]

print(result if result else 0)