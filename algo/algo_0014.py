# 연습 문제 15
# 모든 정점을 너비우선탐색하여 경로를 출력하세요. 시작 정점은 1이다.
from collections import deque

roads = [int(x) for x in input().split()]
graphs = [[] for _ in range((len(roads)//2)+1)]

for i in range(len(roads)//2):
    graphs[roads[2*i]].append(roads[2*i+1])

start = 1
queue = deque()
visited = [False] * (len(roads)//2 + 1)

queue.append(start)
visited[start] = True

while queue:
    now = queue.popleft()
    print(now, end=' ')
    for i in graphs[now]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
print()