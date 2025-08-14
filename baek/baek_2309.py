# 2309. 일곱 난쟁이

nan = []
for i in range(9):
    nan.append(int(input()))

total = sum(nan)

visited = [False] * 9

find_nan = False
for i in range(9):
    if find_nan:
        break
    for j in range(i+1, 9):
        if total - nan[i] - nan[j] == 100:
            idx_1, idx_2 = i, j
            find_nan = True
            break

result = []
for i, n in enumerate(nan):
    if i != idx_1 and i != idx_2:
        result.append(n)
result.sort()
for r in result:
    print(r)