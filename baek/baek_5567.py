from collections import deque

# 5567. 결혼식

N = int(input())
M = int(input())
graphs = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

start = 1
queue = deque()
queue.append(start)
visited[start] = 0

while queue:
    now = queue.popleft()

    for f in graphs[now]:
        if visited[f] < 0:
            visited[f] = visited[now] + 1
            queue.append(f)

friend = 0
for i in visited:
    if 1 <= i <= 2:
        friend += 1

print(friend)