# 백만 장자 프로젝트
T = int(input())

for t in range(1, T+1):
    N = int(input())
    mm = [int(x) for x in input().split()]

    my_wallet = [0] * N

    idx = N-1
    max_value = 0
    while idx >= 0:
        if idx == N-1:
            max_value = mm[idx]
        else:
            if max_value >= mm[idx]:
                my_wallet[idx] = max_value - mm[idx]
            else:
                max_value = mm[idx]
        idx -= 1

    result = sum(my_wallet)
    print(f'#{t} {result}')