T = 10

for test_case in range(1, T + 1):

    # 1219. 길찾기
    t, N = map(int, input().split())
    road = [int(x) for x in input().split()]

    graph = [[] for _ in range(100)]
    visited = [False] * (100)

    for i in range(N):
        graph[road[2*i]].append(road[2*i+1])

    can_reach = False

    def dfs(now):
        global can_reach

        # 도착점에 도달했다면, 종료!
        if now == 99:
            can_reach = True
            return
        
        for g in graph[now]:
            if not visited[g]:
                visited[now] = True
                dfs(g)
                visited[now] = False

    dfs(0)

    print(f'#{t} {1 if can_reach else 0}')

    