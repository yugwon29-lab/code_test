# 숫자를 정렬하자

T = int(input())

for t in range(1, T+1):
    N = int(input())
    array = [int(x) for x in input().split()]

    for i in range(N):
        min_value = array[i]
        min_idx = i
        
        for j in range(i+1, N):
            if min_value > array[j]:
                min_value = array[j]
                min_idx = j

        if i != min_idx:
            array[i], array[min_idx] = array[min_idx], array[i]

    print(f'#{t}', end=' ')
    print(*array)