# 등산로 조성
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    san = [[int(x) for x in input().split()] for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    max_height = 0
    for i in range(N):
        for j in range(N):
            max_height = max(max_height, san[i][j])

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    max_length = 0
    def walk(i, j, length, chance):
        global max_length, san, visited
        
        can_go = False
        for m in move:
            ni, nj = i + m[0], j + m[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if chance and san[i][j] <= san[ni][nj]:
                    if san[ni][nj] - K < san[i][j]:
                        temp = san[ni][nj]
                        san[ni][nj] = san[i][j] - 1
                        visited[ni][nj] = True
                        chance -= 1
                        walk(ni, nj, length + 1, chance)
                        chance += 1
                        visited[ni][nj] = False
                        san[ni][nj] = temp
                        can_go = True
                elif san[i][j] > san[ni][nj]:
                    visited[ni][nj] = True
                    walk(ni, nj, length + 1, chance)
                    visited[ni][nj] = False
                    can_go = True
        
        if not can_go:
            max_length = max(length, max_length)

    for i in range(N):
        for j in range(N):
            if san[i][j] == max_height:
                visited[i][j] = True
                walk(i, j, 1, 1)
                visited[i][j] = False
    
    print(f'#{t}', max_length)
        
