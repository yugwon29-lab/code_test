N, M, K = map(int, input().split())
board_1 = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r, c = r - 1, c - 1
    board_1[r][c].append((m, s, d))

direct = [(-1, 0), (-1, 1), (0, 1), (1, 1),
          (1, 0), (1, -1), (0, -1), (-1, -1)]

for k in range(K):
    board_2 = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for fire in board_1[i][j]:
                m, s, d = fire
                move = direct[d]
                dr, dc = move[0] * s, move[1] * s
                r, c = (i + dr) % N, (j + dc) % N
                board_2[r][c].append((m, s, d))
    
    board_1 = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(board_2[i][j]) >= 2:
                total_m = 0
                total_s = 0
                all_odd = True
                all_eve = True
                for fire in board_2[i][j]:
                    m, s, d = fire
                    total_m += m
                    total_s += s
                    if d % 2 == 0:
                        all_odd = False
                    else:
                        all_eve = False
                m = total_m // 5
                if m == 0:
                    continue
                s = total_s // len(board_2[i][j])
                if all_odd or all_eve:
                    di = [0, 2, 4, 6]
                else:
                    di = [1, 3, 5, 7]

                for d in di:
                    board_1[i][j].append((m, s, d))
            else:
                for fire in board_2[i][j]:
                    m, s, d = fire
                    board_1[i][j].append((m, s, d))

total_m = 0
for i in range(N):
    for j in range(N):
        for fire in board_1[i][j]:
            m, s, d = fire
            total_m += m

print(total_m)