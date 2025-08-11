from collections import deque

# 15655. N과 M (8)
N, M = map(int, input().split())
number = [int(x) for x in input().split()]
number.sort()

# 사용 여부
def dfs(num_list):

    if len(num_list) >= 2 and num_list[-2] > num_list[-1]:
        return

    if len(num_list) == M:
        print(*num_list)
        return
    
    for i in range(N):
        dfs(num_list + [number[i]])

dfs([])
