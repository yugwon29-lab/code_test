# 최적 경로
T = int(input())

for t in range(1, T+1):
    N = int(input())
    xys = [int(x) for x in input().split()]
    others = []

    for i in range(N+2):
        if i == 0:
            com_x, com_y = xys[2*i], xys[2*i+1]
        elif i == 1:
            hom_x, hom_y = xys[2*i], xys[2*i+1]
        else:
            x, y = xys[2*i], xys[2*i+1]
            others.append((x, y))

    visited = [False] * N
    min_dist = 9999999
    def distance(cur, num, dist):
        global min_dist
        if cur == N:
            to_home = abs(hom_x - others[num][0]) + abs(hom_y - others[num][1])
            dist = dist + to_home
            if dist < min_dist:
                min_dist = dist
            return
        
        for i in range(N):
            if not visited[i]:
                to_dist = abs(others[num][0] - others[i][0]) + abs(others[num][1] - others[i][1])
                visited[i] = True
                distance(cur+1, i, dist+to_dist)
                visited[i] = False

    for i in range(N):
        to_dist = abs(com_x - others[i][0]) + abs(com_y - others[i][1])
        visited[i] = True
        distance(1, i, to_dist)
        visited[i] = False

    print(f'#{t}', min_dist)