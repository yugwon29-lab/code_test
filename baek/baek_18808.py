# 18808. 스티커 붙이기
N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [[int(x) for x in input().split()] for _ in range(R)]
    stickers.append(((R, C), sticker))

notebook = [[0] * M for _ in range(N)]

def turn(sticker):
    R, C = sticker[0]
    sticker = sticker[1]
    turn_sticker = []
    for j in range(C):
        row = []
        for i in range(R-1, -1, -1):
            row.append(sticker[i][j])
        turn_sticker.append(row)
    return ((C, R), turn_sticker)

def stick(i, j, sticker):
    R, C = sticker[0]
    sticker = sticker[1]

    # 0, 90, 180, 270도 회전
    if R + i > N or C + j > M:
        can_stick = False
    else:
        can_stick = True
        for r in range(R):
            for c in range(C):
                ni, nj = i + r, j + c
                if not (0 <= ni < N and 0 <= nj < M):
                    continue
                if sticker[r][c] == notebook[ni][nj] == 1:
                    can_stick = False

    if can_stick:
        for r in range(R):
            for c in range(C):
                ni, nj = i + r, j + c
                if not (0 <= ni < N and 0 <= nj < M):
                    continue
                if notebook[ni][nj] == 0:
                    notebook[ni][nj] = sticker[r][c]
    
    return can_stick

def total_stick(sticker):
    for d in range(4):
        for i in range(N):
            for j in range(M):
                can_stick = stick(i, j, sticker)
                if can_stick:
                    return
        sticker = turn(sticker)
            
for sticker in stickers:
    total_stick(sticker)

total_cnt = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] == 1:
            total_cnt += 1

print(total_cnt)