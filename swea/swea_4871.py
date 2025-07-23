T = int(input())

for i in range(1, T + 1):

    # 4871.그래프 경로
    V, E = map(int, input().split())

    # 경로가 저장된 딕셔너리
    route = {}
    visited = {}
    for j in range(V):
        route[j+1] = []
        visited[j+1] = False

    # 경로 설정
    for j in range(E):
        A, B = map(int, input().split())
        route[A].append(B)
        
    # 시작점과 끝점
    S, G = map(int, input().split())

    # Stack
    stack = []

    # 경로 탐색
    v = S
    # 시작점 방문처리
    visited[v] = True
    while visited[v]:
        # v와 이어진 경로가 있는지 확인
        if len(route[v]) == 0:
            # 없다면, stack에 남은 것이 있나 확인.
            if len(stack) == 0:
                # 없다면, 탐색 완료
                break
            else:
                # 남아 있다면, pop 수행
                v = stack.pop(-1)
                continue
        else:
            all_true = True
            for j in route[v]:
                if not visited[j]:
                    all_true = False
                    stack.append(v)
                    v = j
                    visited[v] = True
                    break
            if all_true:
                if len(stack) == 0:
                    # 없다면, 탐색 완료
                    break
                else:
                    # 남아 있다면, pop 수행
                    v = stack.pop(-1)
                    continue

    if visited[G]:
        print(f"#{i} 1")
    else:
        print(f"#{i} 0")
