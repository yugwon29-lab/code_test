# 그래프 경로

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    graphs = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graphs[a].append(b)
    
    S, G = map(int, input().split())

    visited = [False] * (V+1)

    def dfs(v):
        visited[v] = True

        for w in graphs[v]:
            if not visited[w]:
                dfs(w)

    dfs(S)

    print(f'#{t} {1 if visited[G] else 0}')

