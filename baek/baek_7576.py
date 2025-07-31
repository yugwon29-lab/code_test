# 7576. 토마토

# # 입력 받기
# M, N = map(int, input().split())
# tomato = [[int(x) for x in input().split()] for _ in range(N)]

# # 이동 방향 설정
# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# # 거리 배열 생성
# dist = [[-1 for _ in range(M)] for _ in range(N)]

# # 시작 지점 설정
# queue = []

# for n in range(N):
#     for m in range(M):
#         # 익은 토마토이면, 큐에 추가하기
#         if tomato[n][m] == 1:
#             dist[n][m] = 0
#             queue.append((n, m))

# # BFS
# while len(queue) != 0:
#     i, j = queue.pop(0)

#     # 이동 가능한 모든 경우의 수 확인
#     for m in move:
#         next_i, next_j = i + m[0], j + m[1]
#         # 상자 범위 밖이면 continue
#         if (0 <= next_i < N) and (0 <= next_j < M):
#             # 토마토가 아직 익지 않았다면 익고 큐에 추가하기
#             if dist[next_i][next_j] == -1 and tomato[next_i][next_j] != -1:
#                 dist[next_i][next_j] = dist[i][j] + 1
#                 queue.append((next_i, next_j))
#         else:
#             continue

# # 결과 제출
# all_tomato = True
# max_value = -1
# for n in range(N):
#     for m in range(M):
#         # 익지 않은 토마토가 있음.
#         if dist[n][m] == -1 and tomato[n][m] == 0:
#             all_tomato = False
#         if dist[n][m] > max_value:
#             max_value = dist[n][m]

# if all_tomato:
#     print(max_value)
# else:
#     print(-1)


from collections import deque

# 입력 받기
M, N = map(int, input().split())
tomato = [[int(x) for x in input().split()] for _ in range(N)]

# 이동 방향 설정
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 거리 배열 생성
dist = [[-1 for _ in range(M)] for _ in range(N)]

# 시작 지점 설정
queue = deque()

for n in range(N):
    for m in range(M):
        # 익은 토마토이면, 큐에 추가하기
        if tomato[n][m] == 1:
            dist[n][m] = 0
            queue.append((n, m))

# BFS
while len(queue) != 0:
    i, j = queue.popleft()

    # 이동 가능한 모든 경우의 수 확인
    for m in move:
        next_i, next_j = i + m[0], j + m[1]
        # 상자 범위 밖이면 continue
        if (0 <= next_i < N) and (0 <= next_j < M):
            # 토마토가 아직 익지 않았다면 익고 큐에 추가하기
            if dist[next_i][next_j] == -1 and tomato[next_i][next_j] != -1:
                dist[next_i][next_j] = dist[i][j] + 1
                queue.append((next_i, next_j))
        else:
            continue

# 결과 제출
all_tomato = True
max_value = -1
for n in range(N):
    for m in range(M):
        # 익지 않은 토마토가 있음.
        if dist[n][m] == -1 and tomato[n][m] == 0:
            all_tomato = False
        if dist[n][m] > max_value:
            max_value = dist[n][m]

if all_tomato:
    print(max_value)
else:
    print(-1)