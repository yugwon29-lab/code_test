from collections import deque

# 1012. 유기농 배추

# 입력 받기
T = int(input())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for test_case in range(T):
    M, N, K = map(int, input().split())
    area = [[0 for _ in range(M)] for _ in range(N)]

    # 배추 심기
    for _ in range(K):
        j, i = map(int, input().split())
        area[i][j] = 1

    check = [[-1 for _ in range(M)] for _ in range(N)]
    
    # 지렁이 수
    num = 0

    for n in range(N):
        for m in range(M):
            # 배추가 심어져 있고, 체크하지 않은 곳이면,
            if area[n][m] == 1 and check[n][m] == -1:
                # BFS 시작
                queue = deque()

                check[n][m] = 1
                queue.append((n, m))

                # 새로운 구역이므로, 지렁이 추가
                num += 1

                while len(queue) != 0:
                    i, j = queue.popleft()

                    for m in move:
                        next_i, next_j = i + m[0], j + m[1]
                        
                        # 주변에 배추가 심어져 있는지?
                        if (0 <= next_i < N) and (0 <= next_j < M) and area[next_i][next_j] == 1:
                            # 체크하지 않은 곳이라면, 구역 확장
                            if check[next_i][next_j] == -1:
                                check[next_i][next_j] = 1
                                queue.append((next_i, next_j))

    print(num)
