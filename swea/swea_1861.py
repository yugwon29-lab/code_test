T = int(input())

for test_case in range(1, T + 1):

    # 1861. 정사각형 방
    N = int(input())

    rooms = [[int(x) for x in input().split()] for _ in range(N)]


    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    max_rooms = 0
    min_num = N * N + 1

    dp = [[0] * N for _ in range(N)]
                     
    def dfs(i, j):
        if dp[i][j]:
            return dp[i][j]
        
        dp[i][j] = 1
        now_num = rooms[i][j]
        
        for m in move:
            next_i, next_j = i + m[0], j + m[1]
            if (0 <= next_i < N) and (0 <= next_j < N):
                diff = now_num - rooms[next_i][next_j]
                if (diff == -1):
                    dp[i][j] = max(dp[i][j], dfs(next_i, next_j) + 1)
        
        return dp[i][j]

    for m in range(N):
        for n in range(N):
            length = dfs(m, n)
            if length > max_rooms:
                max_rooms = length
                min_num = rooms[m][n]
            elif length == max_rooms:
                min_num = min(min_num, rooms[m][n])
    
    print(f'#{test_case} {min_num} {max_rooms}')