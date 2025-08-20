# 1325. 효율적인 해킹
from collections import deque

N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graphs[b].append(a)

hack = [-1] * (N+1)

max_computer = 0
max_list = list()
for n in range(1, N+1):
    if hack[n] != -1:
        # 이미 누군가를 신뢰함으로써 값이 구해졌으므로 최대에 속하지는 않는다.
        continue
    start = n
    queue = deque()
    hack[n] = 0

    while queue:
        now = queue.popleft()
        hack[n] += 1

        for g in graphs[n]:
            queue.append(g)

max_list.sort()
print(*max_list)