# 회문1

T = 10

for t in range(1, T+1):
    # 입력 받기
    length = int(input())
    board = [[x for x in input()] for _ in range(8)]

    cnt_palin = 0

    # 가로 먼저 탐색
    for i in range(8):
        for j in range(8-length+1):
            is_palin = True
            for k in range(length // 2):
                if board[i][j+k] != board[i][j+length-k-1]:
                    is_palin = False
                    break
            if is_palin:
                cnt_palin += 1

    # 세로 먼저 탐색
    for j in range(8):
        for i in range(8-length+1):
            is_palin = True
            for k in range(length // 2):
                if board[i+k][j] != board[i+length-k-1][j]:
                    is_palin = False
                    break
            if is_palin:
                cnt_palin += 1

    print(f'#{t} {cnt_palin}')