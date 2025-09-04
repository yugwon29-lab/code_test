# 1767. 프로세서 연결하기

T = int(input())

for t in range(1, T+1):
    N = int(input())
    chip = [[int(x) for x in input().split()] for _ in range(N)]
    cores = []

    # Core 위치 저장
    for i in range(N):
        for j in range(N):
            if chip[i][j] == 1:
                cores.append((i, j))

    # 코어에 대해 전선 연결하기
    max_chip = 0
    min_line = None
    line_map = [[False] * N for _ in range(N)]

    dir_dict = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }

    def check_line(i, j, dir):
        can_line = True
        while True:
            i, j = i + dir_dict[dir][0], j + dir_dict[dir][1]
            if not (0 <= i < N and 0 <= j < N):
                break
            if chip[i][j] == 1 or line_map[i][j]:
                can_line = False
                break
        return can_line
    
    def draw_line(i, j, dir):
        global line_map
        cnt = 0
        while True:
            i, j = i + dir_dict[dir][0], j + dir_dict[dir][1]
            if not (0 <= i < N and 0 <= j < N):
                break
            line_map[i][j] = not line_map[i][j]
            cnt += 1
        return cnt
    
    def lining(idx, chip, line):
        global max_chip, min_line, line_map
        # 모든 칩 연결이 끝난 경우
        if idx == len(cores):
            if chip > max_chip:
                max_chip = chip
                min_line = line
            elif chip == max_chip:
                min_line = min(min_line, line) if min_line is not None else line
            return

        # 칩이 가장자리에 있는 경우, 연결 처리
        if cores[idx][0] == 0 or cores[idx][0] == N-1 \
            or cores[idx][1] == 0 or cores[idx][1] == N-1:
            lining(idx+1, chip+1, line)
        else:
            # 그렇지 않은 경우, 상하좌우로 연결 시도
            i, j = cores[idx][0], cores[idx][1]
            if check_line(i, j, 0):
                n = draw_line(i, j, 0)
                lining(idx+1, chip+1, line+n)
                draw_line(i, j, 0)
            if check_line(i, j, 1):
                n = draw_line(i, j, 1)
                lining(idx+1, chip+1, line+n)
                draw_line(i, j, 1)
            if check_line(i, j, 2):
                n = draw_line(i, j, 2)
                lining(idx+1, chip+1, line+n)
                draw_line(i, j, 2)
            if check_line(i, j, 3):
                n = draw_line(i, j, 3)
                lining(idx+1, chip+1, line+n)
                draw_line(i, j, 3)
            # 칩에 선 연결하지 않은 경우
            lining(idx+1, chip, line)

    lining(0, 0, 0)

    print(f'#{t} {min_line}')



        