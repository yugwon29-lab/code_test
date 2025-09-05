# 14503. 로봇 청소기
N, M = map(int, input().split())
R, C, D = map(int, input().split())

room = [[int(x) for x in input().split()] for _ in range(N)]

move_dict = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

cleaned = [[False] * M for _ in range(N)]

clean = 0
i, j = R, C

def check_clean(i, j):
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    is_clean = True
    for m in move:
        ni, nj = i + m[0], j + m[1]
        if 0 <= ni < N and 0 <= nj < M:
            if not cleaned[ni][nj] and room[ni][nj] != 1:
                is_clean = False
                break
    return is_clean

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not cleaned[i][j]:
        cleaned[i][j] = True
        clean += 1
    # 현재 칸 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if not check_clean(i, j):
        # 반시계 방향으로 90도 회전
        while True:
            D = (D - 1) % 4
            ni, nj = i + move_dict[D][0], j + move_dict[D][1]
            if 0 <= ni < N and 0 <= nj < M:
                if not cleaned[ni][nj] and room[ni][nj] != 1:
                    i, j = ni, nj
                    break
    else:
        ni, nj = i - move_dict[D][0], j - move_dict[D][1]
        if not (0 <= ni < N and 0 <= nj < M) or room[ni][nj] == 1:
            break
        i, j = ni, nj

print(clean)