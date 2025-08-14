# 길찾기

T = 10

for t in range(1, T+1):
    V = 100
    test_num, E = map(int, input().split())
    graphs = [[] for _ in range(V+1)]

    edges = [int(x) for x in input().split()]

    for i in range(E):
        graphs[edges[i*2]].append(edges[i*2+1])
    
    S, G = 0, 99

    visited = [False] * (V+1)

    def dfs(v):
        visited[v] = True
        if visited[G]:
            return

        for w in graphs[v]:
            if not visited[w]:
                dfs(w)

    dfs(S)

    print(f'#{t} {1 if visited[G] else 0}')

