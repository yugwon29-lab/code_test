from collections import deque

# 2667. 단지번호붙이기

# 입력 받기
N = int(input())
board = [[int(x) for x in input()] for _ in range(N)]

# 근처
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 단지 수 리스트 및 확인 여부
village_cnt = []
check = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and check[i][j] == -1:
            # 시작점
            queue = deque()
            cnt = 0

            check[i][j] = 1
            queue.append((i, j))

            while len(queue) != 0:
                now_i, now_j = queue.popleft()
                cnt += 1

                for m in move:
                    next_i, next_j = now_i + m[0], now_j + m[1]
                    if (0 <= next_i < N) and (0 <= next_j < N):
                        if board[next_i][next_j] == 1 and check[next_i][next_j] == -1:
                            check[next_i][next_j] = 1
                            queue.append((next_i, next_j))

            village_cnt.append(cnt)

village_cnt.sort()
print(len(village_cnt))
for c in village_cnt:
    print(c)
