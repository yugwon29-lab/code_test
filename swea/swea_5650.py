T = int(input())

for test_case in range(1, T + 1):

    # 5650. 핀볼 게임
    N = int(input())
    area = [[int(x) for x in input().split()] for y in range(N)]

    # 상하좌우 (0, 1, 2, 3)
    dir_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    bounce_dict = {
        1 : [1, 3, 0, 2],
        2 : [3, 0, 1, 2],
        3 : [2, 0, 3, 1],
        4 : [1, 2, 3, 0],
        5 : [1, 0, 3, 2],
    }

    hole_dict = {}

    # 웜홀 탐색
    for i in range(N):
        for j in range(N):
            if 6 <= area[i][j] <= 10:
                if area[i][j] not in hole_dict:
                    hole_dict[area[i][j]] = (i, j)
                else:
                    hole_dict[(i, j)] = hole_dict[area[i][j]]
                    hole_dict[hole_dict[area[i][j]]] = (i, j)
                    hole_dict.pop(area[i][j])

    # 최대 점수
    max_score = 0

    def pin_ball(i, j, dir):

        si, sj, dir = i, j, dir
        score = 0 
        
        while True:
            # dir 방향대로 이동한다.
            ni, nj = i + dir_list[dir][0], j + dir_list[dir][1]
            
            # 벽에 부딪힌 경우
            if not (0 <= ni < N and 0 <= nj < N) or area[ni][nj] == 5:
                i, j = ni, nj
                dir = bounce_dict[5][dir]
                score += 1
                continue
            
            if (ni, nj) == (si, sj) or area[ni][nj] == -1:
                return score
            
            # 물체에 부딪힌 경우
            if 1 <= area[ni][nj] <= 4:
                dir = bounce_dict[area[ni][nj]][dir]
                score += 1
                i, j = ni, nj
                continue 
            
            # 웜홀에 빠진 경우
            if 6 <= area[ni][nj] <= 10:
                ni, nj = hole_dict[(ni, nj)]
                i, j = ni, nj
                continue
            
            i, j = ni, nj

    for i in range(N):
        for j in range(N):
            if area[i][j] == 0:
                for d in [0, 1, 2, 3]:
                    max_score = max(max_score, pin_ball(i, j, d))

    print(f'#{test_case} {max_score}')
    