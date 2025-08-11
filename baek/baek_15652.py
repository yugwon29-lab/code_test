from collections import deque

# 15651. N과 M (4)
N, M = map(int, input().split())

def dfs(num_list, i=1):
    if len(num_list) == M:
        print(*num_list)
        return
    
    for k in range(i, N+1):
        dfs(num_list+[k], k)

dfs([])