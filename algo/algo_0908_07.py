# 벽돌 깨기
from collections import deque
from copy import deepcopy

T = int(input())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for t in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [[int(x) for x in input().split()] for _ in range(H)]

    # 남은 블록 세는 함수
    def cnt_brick(board):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if board[i][j] != 0:
                    cnt += 1
        return cnt
    
    # 중력 적용
    def fall_brick(board):
        for j in range(W):
            stack = deque()
            for i in range(H-1, -1, -1):
                if board[i][j] != 0:
                    stack.append(board[i][j])
            for i in range(H-1, -1, -1):
                if len(stack) > 0:
                    board[i][j] = stack.popleft()
                else:
                    board[i][j] = 0
        return board

    # j열에 구술 발사
    min_brick = None
    def shot(cur, j, my_board):
        global min_brick
        original = deepcopy(my_board)

        def bfs(i, j, now_board):
            queue = deque()
            queue.append((i, j))

            while queue:
                i, j = queue.popleft()
                brick_num = now_board[i][j]
                now_board[i][j] = 0
                for n in range(1, brick_num):
                    for m in move:
                        ni, nj = i + m[0] * n, j + m[1] * n
                        if 0 <= ni < H and 0 <= nj < W:
                            queue.append((ni, nj))
            return now_board

        if cur == N:
            min_brick = min(min_brick, cnt_brick(my_board)) if min_brick is not None else cnt_brick(my_board)
            return
        
        i = 0
        while i < H and my_board[i][j] == 0:
            i += 1

        if i < H:
            my_board = bfs(i, j, my_board)
            my_board = fall_brick(my_board)

        for k in range(W):
            shot(cur+1, k, my_board)
            my_board = deepcopy(original)

    for k in range(W):
        my_board = deepcopy(board)
        shot(0, k, board)

    print(f'#{t} {min_brick}')

