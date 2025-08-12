# 24479. 알고리즘 수업 - 깊이 우선 탐색 1
from collections import deque

N, M, R = map(int, input().split())

nodes = []
graphs = [[] for _ in range(N+1)]

for n in range(M):
    x, y = map(int, input().split())
    nodes.append((x, y))

for a, b in nodes:
    graphs[a].append(b)
    graphs[b].append(a)

numbers = [-1] * (N+1)

def dfs(cur, i):

    numbers[i] = cur
    
    for g in graphs[i]:
        if numbers[g] == -1:
            dfs(cur+1, g)

dfs(1, R)

for i in range(1, N+1):
    print(numbers[i] if numbers[i] != -1 else 0)