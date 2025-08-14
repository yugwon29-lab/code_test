# 2448. 별 찍기 - 11

N = int(input())

board = [[' '] * (2 * N - 1) for _ in range(N)]

def star(r, c, n):
    global board
    if n == 3:
        board[r][c] = '*'
        board[r+1][c-1] = board[r+1][c+1] = '*'
        for i in range(-2, 3):
            board[r+2][c+i] = '*'
        return
    half = n // 2
    star(r, c, half)
    star(r+half, c-half, half)
    star(r+half, c+half, half)

star(0, (2 * N - 1)//2, N)

for i in range(N):
    print(''.join(board[i]))