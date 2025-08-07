# 어디에 단어가 들어갈 수 있을까

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    array = [[int(x) for x in input().split()] for _ in range(N)]

    num_word = 0

    # 가로 탐색
    for i in range(N):
        cnt_white = 0
        for j in range(N):
            if array[i][j] == 1:
                cnt_white += 1
            else:
                if cnt_white == K:
                    num_word += 1
                cnt_white = 0
        if cnt_white == K:
            num_word += 1

    # 세로로 탐색
    for j in range(N):
        cnt_white = 0
        for i in range(N):
            if array[i][j] == 1:
                cnt_white += 1
            else:
                if cnt_white == K:
                    num_word += 1
                cnt_white = 0
        if cnt_white == K:
            num_word += 1

    print(f'#{t} {num_word}')