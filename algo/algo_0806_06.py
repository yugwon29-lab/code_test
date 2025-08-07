# Sum

T = 10

for t in range(1, T+1):
    n = int(input())
    board = [[int(x) for x in input().split()] for _ in range(100)]
    
    max_v = 0
    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v += board[i][j]
        if max_v < sum_v:
            max_v = sum_v
    
    for j in range(100):
        sum_v = 0
        for i in range(100):
            sum_v += board[i][j]
        if max_v < sum_v:
            max_v = sum_v

    sum_v = 0
    for i in range(100):
        sum_v += board[i][i]
    if max_v < sum_v:
        max_v = sum_v

    sum_v = 0
    for i in range(100):
        sum_v += board[i][-i-1]
    if max_v < sum_v:
        max_v = sum_v

    print(f'#{n} {max_v}')
        