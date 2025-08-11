from collections import deque

# 15651. N과 M (3)
N, M = map(int, input().split())

def dfs(num_list):
    if len(num_list) == M:
        print(*num_list)
        return
    
    for i in range(1, N+1):
        dfs(num_list + [i])

dfs([])
    