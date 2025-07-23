T = int(input())

for i in range(1, T + 1):

    # 4874. 미로
    N = int(input())
    S = [[int(x) for x in input()] for y in range(N)]
    V = [[False for j in range(N)] for k in range(N)]

    point_stack = []
    # move_stack = []
    start, end = None, None
    # 시작 위치 (r,c), 이동방향 저장
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 0 : 상, 1 : 하, 2 : 좌, 3 : 우

    # 시작 지점 및 끝 지점 설정
    for j in range(N):
        for k in range(N):
            if S[j][k] == 2:
                start = (j, k)
            elif S[j][k] == 3:
                end = (j, k)
            elif S[j][k] == 1:
                # 통과할 수 없는 영역
                V[j][k] = True

    if start is not None and end is not None:
        now = start
        V[now[0]][now[1]] = True
        while V[now[0]][now[1]]:
            # 현재 위치에서 갈 수 있는 부분이 있는지 확인한다.
            cant_go = True
            for m in move:
                next_j, next_k = now[0] + m[0], now[1] + m[1]
                if not (0 <= next_j < N) or not (0 <= next_k < N):
                    # 밖으로 나갈 수 없다.
                    continue
                else:
                    if not V[next_j][next_k]:
                        # 갈 수 있는 곳이면, 나아간다.
                        point_stack.append(now)
                        cant_go = False
                        # 위치 이동 후, 방문 처리
                        now = (next_j, next_k)
                        V[now[0]][now[1]] = True
                        break
                    else:
                        # 지나갈 수 없다.
                        continue
            if S[now[0]][now[1]] == 3:
                # 탈출구에 도달했다면, 탐색 마치기
                break
            if cant_go:
                # 현 위치에서 나아갈 수 없다면, 되돌아간다.
                if len(point_stack) == 0:
                    # 되돌아갈 곳이 없다면, 탐색 마치기
                    break
                else:
                    now = point_stack.pop()

        if V[end[0]][end[1]]:     
            print(f"#{i} 1")
        else:
            print(f"#{i} 0")        

    else:
        print(f"#{i} error")
