from collections import deque

# 15655. N과 M (6)
N, M = map(int, input().split())
number = [int(x) for x in input().split()]
number.sort()

# 사용 여부
is_used = [False] * N

def dfs(num_list):

    if len(num_list) >= 2 and num_list[-2] >= num_list[-1]:
        return

    if len(num_list) == M:
        print(*num_list)
        return
    
    for i in range(N):
        if not is_used[i]:
            is_used[i] = True
            dfs(num_list + [number[i]])
            is_used[i] = False

dfs([])
