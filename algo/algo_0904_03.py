# 최대 상금
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    start = str(N)

    cur_level = {start}

    for _ in range(K):
        next_level = set()
        for num in cur_level:
            num_list = list(num)
            for i in range(len(num_list)-1):
                for j in range(i+1, len(num_list)):
                    if i == j:
                        continue
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    next_level.add(''.join(num_list))
                    num_list[i], num_list[j] = num_list[j], num_list[i]
        cur_level = next_level

    max_money = max(map(int, cur_level))
    print(f'#{t} {max_money}')