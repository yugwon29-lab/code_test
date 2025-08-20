# 1325. 효율적인 해킹
from collections import deque

N, M = map(int, input().split())
graphs = [[] * (N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graphs[b].append(a)

def bfs(i):
    