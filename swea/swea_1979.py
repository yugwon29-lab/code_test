T = int(input())

for test_case in range(1, T + 1):

    # 1979. 어디에 단어가 들어갈 수 있을까
    N, K = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(N)]

    count = 0
    for i in range(N):
        white_cnt = 0
        for j in range(N):
            if board[i][j] == 1:
                white_cnt += 1
            else:
                if K == white_cnt:
                    count += 1
                white_cnt = 0
        if K == white_cnt:
            count += 1
    
    for i in range(N):
        white_cnt = 0
        for j in range(N):
            if board[j][i] == 1:
                white_cnt += 1
            else:
                if K == white_cnt:
                    count += 1
                white_cnt = 0
        if K == white_cnt:
            count += 1

    print(f'#{test_case} {count}')