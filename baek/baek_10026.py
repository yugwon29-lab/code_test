from collections import deque

# 10026. 적록색약

# 입력 받기
N = int(input())
tv = [[c for c in input()] for _ in range(N)]

# 이동
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 정상
color_3 = [[-1 for _ in range(N)] for _ in range(N)]
# 적록색약
color_2 = [[-1 for _ in range(N)] for _ in range(N)]

num_3, num_2 = 0, 0

for i in range(N):
    for j in range(N):
        # 현재 컬러 저장
        now_color = tv[i][j]
        if color_3[i][j] == -1:         
            # 정상
            num_3 += 1

            # 시작점 설정
            color_3[i][j] = 1
            
            queue = deque()
            queue.append((i, j))

            while len(queue) != 0:
                now_i, now_j = queue.popleft()

                for m in move:
                    next_i, next_j = now_i + m[0], now_j + m[1]
                    # 색이 같고, 범위 내이며, 체크 안한 상태라면,
                    if (0 <= next_i < N) and (0 <= next_j < N) and tv[next_i][next_j] == now_color:
                        if color_3[next_i][next_j] == -1:
                            color_3[next_i][next_j] = 1
                            queue.append((next_i, next_j))
                    else:
                        continue
        if color_2[i][j] == -1:         
            # 적록색약
            num_2 += 1

            # 시작점 설정
            color_2[i][j] = 1
            
            queue = deque()
            queue.append((i, j))

            while len(queue) != 0:
                now_i, now_j = queue.popleft()

                for m in move:
                    next_i, next_j = now_i + m[0], now_j + m[1]
                    # 색이 같고, 범위 내이며, 체크 안한 상태라면,
                    if (0 <= next_i < N) and (0 <= next_j < N):
                        if (now_color in 'RG' and tv[next_i][next_j] in 'RG') or now_color == tv[next_i][next_j]:
                            if color_2[next_i][next_j] == -1:
                                color_2[next_i][next_j] = 1
                                queue.append((next_i, next_j))
                    else:
                        continue

print(num_3, num_2)