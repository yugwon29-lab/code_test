from collections import deque

# 5663. N과 M (10)
N, M = map(int, input().split())
number = [int(x) for x in input().split()]
number.sort()

num_dict = {}
for n in number:
    num_dict[n] = num_dict.get(n, 0) + 1

unique = list(num_dict.keys())

# 사용 여부
def dfs(num_list):

    if len(num_list) >= 2 and num_list[-2] > num_list[-1]:
        return

    if len(num_list) == M:
        print(*num_list)
        return
    
    for u in unique:
        if num_dict[u] == 0:
            continue
        num_dict[u] -= 1
        dfs(num_list+[u])
        num_dict[u] += 1
    

dfs([])
