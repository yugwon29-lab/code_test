# 1799. 비숍
N = int(input())
chess = [[int(x) for x in input().split()] for _ in range(N)]

# 흑과 백으로 나눈다.
white = []
black = []
for i in range(N):
    for j in range(N):
        if chess[i][j] == 1:
            ru, rd = i + j, N - 1 - (i - j)
            if ru % 2 == 0:
                white.append((ru, rd))
            else:
                black.append((ru, rd))

is_used_ru = [0] * (2 * N - 1)
is_used_rd = [0] * (2 * N - 1)

max_bishop_w = 0
max_bishop_b = 0

def white_bishop(cur, bishop_w):
    global max_bishop_w
    if cur == len(white):
        max_bishop_w = max(max_bishop_w, bishop_w)
        return
    
    # 현재 위치에 두는 경우
    now_ru, now_rd = white[cur]
    if not (is_used_rd[now_rd] or is_used_ru[now_ru]):
        is_used_rd[now_rd], is_used_ru[now_ru] = True, True
        white_bishop(cur+1, bishop_w+1)
        is_used_rd[now_rd], is_used_ru[now_ru] = False, False

    # 두지 않는 경우
    white_bishop(cur+1, bishop_w)

def black_bishop(cur, bishop_b):
    global max_bishop_b
    if cur == len(black):
        max_bishop_b = max(max_bishop_b, bishop_b)
        return
    
    # 현재 위치에 두는 경우
    now_ru, now_rd = black[cur]
    if not (is_used_rd[now_rd] or is_used_ru[now_ru]):
        is_used_rd[now_rd], is_used_ru[now_ru] = True, True
        black_bishop(cur+1, bishop_b+1)
        is_used_rd[now_rd], is_used_ru[now_ru] = False, False

    # 두지 않는 경우
    black_bishop(cur+1, bishop_b)

white_bishop(0, 0)
black_bishop(0, 0)

print(max_bishop_w + max_bishop_b)

