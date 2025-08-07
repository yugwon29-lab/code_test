# Ladder1

T = 10

for t in range(1, T+1):
    N = int(input())
    array = [[int(x) for x in input().split()] for _ in range(100)]

    for j in range(100):
        if array[0][j] == 0:
            continue
        else:
            end_v = -1
            ni, nj = 0, j
            # 아래 우선 탐색
            di, dj = 1, 0
            while ni < 100 - 1:
                if (di, dj) == (1, 0):
                    # 아래로 가고 있는 경우
                    # 좌우를 먼저 살핀다.
                    if nj - 1 >= 0 and array[ni][nj-1] == 1:
                        # 왼쪽이 뚫려 있다면
                        di, dj = 0, -1
                    elif nj + 1 < 100 and array[ni][nj+1] == 1:
                        # 오른쪽이 뚫려 있다면
                        di, dj = 0, 1
                elif (di, dj) == (0, -1):
                    # 왼쪽으로 가는 중일 경우
                    if nj - 1 >= 0 and array[ni][nj-1] == 1:
                        # 왼쪽이 계속 뚫려 있으면 pass
                        pass
                    elif array[ni+1][nj] == 1:
                        di, dj = 1, 0
                elif (di, dj) == (0, 1):
                    # 왼쪽으로 가는 중일 경우
                    if nj + 1 < 100 and array[ni][nj+1] == 1:
                        # 왼쪽이 계속 뚫려 있으면 pass
                        pass
                    elif array[ni+1][nj] == 1:
                        di, dj = 1, 0
                
                ni, nj = ni + di, nj + dj
                    
            end_v = array[ni][nj]

            if end_v == 2:
                print(f'#{t} {j}')
                break
            
