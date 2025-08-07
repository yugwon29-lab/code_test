from collections import deque

# 15650. N과 M (2)

N, M = map(int, input().split())

is_used = [False] * (N + 1)

def dfs(numbers):
    # 종료 조건
    if len(numbers) == M:
        print(*numbers)
    
    if len(numbers) == 0:
        start = 1
    else:
        start = numbers[-1]

    for i in range(start, N+1):
        if not is_used[i]:
            is_used[i] = True
            dfs(numbers+[i])
            is_used[i] = False

dfs([])