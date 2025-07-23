T = int(input())

for i in range(1, T + 1):

    # 4835. 구간합
    N, M = map(int, input().split())
    num_list = [int(x) for x in input().split()]

    for j in range(N - M + 1):
        add_range = range(j, j+M)
        sum = 0
        for add in add_range:
            sum += num_list[add]
       
        if j == 0:
            min_value = sum
            max_value = sum
        else:
            min_value = sum if sum < min_value else min_value
            max_value = sum if sum > max_value else max_value

    result = max_value - min_value

    print(f'#{i} {result}')
