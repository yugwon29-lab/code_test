T = int(input())

for test_case in range(1, T + 1):

    # 4881. 배열 최소 합
    N = int(input())
    array = [[int(x) for x in input().split()] for y in range(N)]

    min_sum = float('inf')
    visited = [False for x in range(N)]

    def dfs(row, total, visited):
        global min_sum

        if row == N:
            min_sum = min(total, min_sum)
            return
        
        if total >= min_sum:
            return
        
        for col in range(N):
            if not visited[col]:
                visited[col] = True
                dfs(row + 1, total + array[row][col], visited)
                visited[col] = False

    dfs(0, 0, visited)
    print(f'#{test_case} {min_sum}')
