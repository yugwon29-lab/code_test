T = int(input())

for test_case in range(1, T + 1):

    # 5102. 노드의 거리
    V, E = map(int, input().split())
    route = {k: [] for k in range(1, V+1)}
    for i in range(E):
        x, y = map(int, input().split())
        route[x].append(y)
        route[y].append(x)
    S, G = map(int, input().split())

    # 방문 기록
    visited = [0] * V

    # 큐
    queue = []

    # 시작점 설정
    start = S
    queue.append(start)
    find_route = False
    cnt = 1
    node = 0
    while queue:
        now = queue.pop(0)
        cnt -= 1
        if not visited[now-1]:
            visited[now-1] = 1
        for r in route[now]:
            next_node = r
            if not visited[next_node-1]:
                queue.append(next_node)
        
        if now == G:
            find_route = True
            break

        if cnt == 0:
            cnt += len(queue)
            node += 1

    if find_route:
        print(f'#{test_case} {node}')
    else:
        print(f'#{test_case} 0')