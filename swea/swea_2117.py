from collections import deque

T = int(input())

for test_case in range(1, T + 1):

    # 2117. 홈 방범 서비스
    
    # 입력 받기
    N, M = map(int, input().split())
    home_map = [[int(x) for x in input().split()] for _ in range(N)]
    
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    max_home = 0

    def bfs(i, j):
        global max_home

        # 거리 배열 설정
        dist = [[-1] * N for _ in range(N)]

        # 출발지 설정
        queue = deque()

        # 서비스 이용 중인 가구 수
        home = 0

        K = 1
        dist[i][j] = K
        queue.append((i, j))

        # BFS
        while queue:
            pi, pj = queue.popleft()

            if home_map[pi][pj] == 1:
                home += 1

            K = dist[pi][pj]
            company = home * M - ((K ** 2) + (K - 1) ** 2)
            if company >= 0:
                if home > max_home:
                    max_home = home

            for m in move:
                ni, nj = pi + m[0], pj + m[1]
                if 0 <= ni < N and 0 <= nj < N:
                    if dist[ni][nj] == -1:
                        dist[ni][nj] = dist[pi][pj] + 1
                        queue.append((ni, nj))
         

    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print(f'#{test_case} {max_home}')