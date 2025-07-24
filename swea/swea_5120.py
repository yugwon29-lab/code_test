T = int(input())

for test_case in range(1, T + 1):

    # 5120. 암호
    N, M, K = map(int, input().split())
    numbers = [int(x) for x in input().split()]

    idx = 0
    for k in range(K):
        next_idx = idx + M
        if next_idx == len(numbers):
            numbers.append(numbers[-1] + numbers[0])
            idx = next_idx
            continue
        elif next_idx > len(numbers):
            while next_idx > len(numbers):
                next_idx -= len(numbers)
        idx = next_idx
        numbers.insert(idx, numbers[idx] + numbers[idx-1])

    for i in range(len(numbers)+1):
        if i == 0:
            print(f'#{test_case}', end=' ')
        elif i == 10 or i == len(numbers):
            print(numbers[-i])
            break
        else:
            print(numbers[-i], end=' ')