# 특별한 정렬

T = int(input())

for t in range(1, T+1):
    N = int(input())
    array = [int(x) for x in input().split()]

    for i in range(5):
        min_value, max_value = float('inf'), -float('inf')
        min_idx, max_idx = -1, -1

        for j in range(2*i, N):
            if max_value < array[j]:
                max_value = array[j]
                max_idx = j

        array[2*i], array[max_idx] = array[max_idx], array[2*i]

        for j in range(2*i+1, N):
            if min_value > array[j]:
                min_value = array[j]
                min_idx = j

        array[2*i+1], array[min_idx] = array[min_idx], array[2*i+1]

    print(f'#{t}', end=' ')
    print(*array[:10])