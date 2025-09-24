# 20057. 마법사 상어와 토네이도
from math import floor

N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]

# 토네이도 이동 방향
direct = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# 토네이도 초기 위치
i, j = N // 2, N // 2
# 토네이도 이동 변수
# 이동 방향 인덱스
d = 0
# 특정 방향으로 이동 횟수
cnt = 0
# 방향 변환 횟수
change_d = 0
d_total = change_d // 2 + 1

# 나간 모래
out_sand = 0

while not (i == 0 and j == 0):
    # 다음 토네이도의 중심지
    move = direct[d]
    ni, nj = i + move[0], j + move[1]

    nxt_sand = A[ni][nj]
    wind_sand = 0
    A[ni][nj] = 0
    for k in range(5):
        if k == 0:
            si_list = [1, -1] if move[0] == 0 else [-move[0]]
            sj_list = [1, -1] if move[1] == 0 else [-move[1]]
            for si in si_list:
                for sj in sj_list:
                    sand = floor(nxt_sand * 0.01)
                    wind_sand += sand
                    if not (0 <= ni + si < N and 0 <= nj + sj < N):
                        out_sand += sand
                    else:
                        A[ni+si][nj+sj] += sand
                    
        elif k == 1:
            si_list = [1, -1] if move[0] == 0 else [0]
            sj_list = [1, -1] if move[1] == 0 else [0]
            for si in si_list:
                for sj in sj_list:
                    sand = floor(nxt_sand * 0.07)
                    wind_sand += sand
                    if not (0 <= ni + si < N and 0 <= nj + sj < N):
                        out_sand += sand
                    else:
                        A[ni+si][nj+sj] += sand
        elif k == 2:
            si_list = [2, -2] if move[0] == 0 else [0]
            sj_list = [2, -2] if move[1] == 0 else [0]
            for si in si_list:
                for sj in sj_list:
                    sand = floor(nxt_sand * 0.02)
                    wind_sand += sand
                    if not (0 <= ni + si < N and 0 <= nj + sj < N):
                        out_sand += sand
                    else:
                        A[ni+si][nj+sj] += sand

        elif k == 3:
            si_list = [1, -1] if move[0] == 0 else [move[0]]
            sj_list = [1, -1] if move[1] == 0 else [move[1]]
            for si in si_list:
                for sj in sj_list:
                    sand = floor(nxt_sand * 0.1)
                    wind_sand += sand
                    if not (0 <= ni + si < N and 0 <= nj + sj < N):
                        out_sand += sand
                    else:
                        A[ni+si][nj+sj] += sand

        elif k == 4:
            si, sj = move[0] * 2, move[1] * 2
            sand = floor(nxt_sand * 0.05)
            wind_sand += sand
            if not (0 <= ni + si < N and 0 <= nj + sj < N):
                out_sand += sand
            else:
                A[ni+si][nj+sj] += sand
    
    si, sj = move
    sand = nxt_sand - wind_sand
    if not (0 <= ni + si < N and 0 <= nj + sj < N):
        out_sand += sand
    else:
        A[ni+si][nj+sj] += sand

    # 이동 관련 처리
    cnt += 1
    if cnt == d_total:
        d = (d + 1) % 4
        change_d += 1
        d_total = change_d // 2 + 1
        cnt = 0

    i, j = ni, nj

print(out_sand)