# 격자판의 숫자 이어 붙이기
T = int(input())

moving = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for t in range(1, T+1):
    board = [[x for x in input().split()] for _ in range(4)]

    my_num = []
    num_set = set()

    def move(i, j):
        if len(my_num) == 7:
            num_set.add("".join(my_num))
            return
        
        for m in moving:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < 4 and 0 <= nj < 4:
                my_num.append(board[ni][nj])
                move(ni, nj)
                my_num.pop()
    
    for i in range(4):
        for j in range(4):
            my_num.append(board[i][j])
            move(i, j)
            my_num.pop()

    print(f'#{t}', len(num_set))
