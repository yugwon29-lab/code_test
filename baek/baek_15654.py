from collections import deque

# 15654. N과 M (5)
N, M = map(int, input().split())
number = [int(x) for x in input().split()]
number.sort()

# 사용 여부
is_used = [False] * N

def dfs(num_list):

    if len(num_list) == M:
        print(*num_list)
        return
    
    for i in range(N):
        if not is_used[i]:
            is_used[i] = True
            dfs(num_list + [number[i]])
            is_used[i] = False

dfs([])
