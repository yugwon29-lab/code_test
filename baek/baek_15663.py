from collections import deque

# 5663. N과 M (9)
N, M = map(int, input().split())
number = [int(x) for x in input().split()]
number.sort()

number_dict = {}
for n in number:
    number_dict[n] = number_dict.setdefault(n, 0) + 1

used_dict = {}

# 사용 여부
def dfs(num_list):

    if len(num_list) == M:
        print(*num_list)
        return
    
    for key in number_dict.keys():
        if used_dict.setdefault(key, 0) < number_dict.setdefault(key, 0):
            used_dict[key] += 1
            dfs(num_list + [key])
            used_dict[key] -= 1

dfs([])
