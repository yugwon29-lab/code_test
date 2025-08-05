T = int(input())

for test_case in range(1, T + 1):

    # 1949. 등산로 조성
    N, K = map(int, input().split())
    array = [[int(x) for x in input().split()] for _ in range(N)]

    # 봉우리 찾기
    max_height = 0
    for i in range(N):
        for j in range(N):
            if max_height < array[i][j]:
                max_height = array[i][j]
    
    # 여기에 최고점 봉우리들의 좌표가 저장된다.
    highest = []
    for i in range(N):
        for j in range(N):
            if max_height == array[i][j]:
                highest.append((i, j))

    # 이동 가능 경우의 수
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_length = 0
    visited = [[-1] * N for _ in range(N)]
        
    def dfs(i, j, cur=1, chance=1):
        global max_length

        if cur > max_length:
            max_length = cur

        for m in move:
            if 0 <= i+m[0] < N and 0 <= j+m[1] < N and visited[i+m[0]][j+m[1]] == -1:
                if array[i][j] > array[i+m[0]][j+m[1]]:
                    visited[i][j] = 1
                    dfs(i+m[0], j+m[1], cur+1, chance)
                    visited[i][j] = -1
                else:
                    if chance and array[i][j] > array[i+m[0]][j+m[1]] - K:
                        original = array[i+m[0]][j+m[1]]
                        array[i+m[0]][j+m[1]] = array[i][j] - 1
                        visited[i][j] = 1
                        dfs(i+m[0], j+m[1], cur+1, chance-1)
                        array[i+m[0]][j+m[1]] = original
                        visited[i][j] = -1
    
    for high in highest:
        i, j = high
        dfs(i, j, 1, 1)

    print(f'#{test_case} {max_length}')