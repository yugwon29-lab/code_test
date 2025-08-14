# 연습 문제 13
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오.

route = [int(x) for x in input().split()]
graph = [[] for _ in range(len(route) + 1)]

for i in range(len(route) // 2):
    graph[route[2*i]].append(route[2*i+1])
    graph[route[2*i+1]].append(route[2*i])

for adj in graph:
    adj.sort()

visited = [False] * (len(route) + 1)
start = 1

def dfs(v):

    visited[v] = True
    print(v, end=' ')

    for w in graph[v]:
        if not visited[w]:
            dfs(w)

dfs(start)
print()