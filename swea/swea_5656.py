# 5656. 벽돌 깨기
from collections import deque
from copy import deepcopy

T = int(input())

for t in range(1, T+1):

    # 입력 받기
    N, W, H = map(int, input().split())
    brick = [[int(x) for x in input().split()] for _ in range(H)]

    # 벽돌 깨기 범위
    break_range = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS
    def bfs(i, num_brick=0):
        global dist

        # i번째 열의 블록을 제거한다.
        find_brick = False
        for r in range(H):
            if brick[r][i] >= 1:
                find_brick = True
                r_brick = r
                break
        
        # 해당 열에 블록이 없다면 패스
        if not find_brick:
            return
        
        # 블록이 있다면, BFS 수행
        sr, sc = r_brick, i
        queue = deque()

        # 처음 블록 깨진다.
        num_brick += 1
        dist[sr][sc] = True
        queue.append((sr, sc))

        while queue:
            r, c = queue.popleft()

            # 벽돌 터트리기
            for k in range(1, brick[r][c]):
                for br in break_range:
                    nr, nc = r + br[0] * k, br[1] * k
                    if 0 <= nr < H and 0 <= nc < W:
                        # 이미 깨진 블록이라면, 위로 탐색
                        if dist[nr][nc]:
                            up = 0
                            while 0 <= nr - up < H:
                                up += 1
                                # 깨지지 않은 벽돌을 찾았다면, 해당 벽돌을 선택한다.
                                if not dist[nr-up][nc] and brick[nr-up][nc] >= 1:
                                    break
                            # 찾지 못했다면, 패스한다.
                            if nr - up < 0:
                                break
                            dist[nr-up][nc] = True
                            num_brick += 1
                            queue.append((nr, nc))
                        else:
                            dist[nr][nc] = True
                            num_brick += 1
                            queue.append((nr, nc))
        
        return num_brick
    
    # 최대 벽돌 수
    max_brick = 0

    # 깨진 벽돌 여부
    dist = [[False for _ in range(W)] for _ in range(H)]


    def dfs(n=0, num_brick=0):
        global dist, max_brick

        # 구슬을 최대한으로 쏘면 그만두기
        if n >= N:
            if num_brick > max_brick:
                max_brick = num_brick
            return
        
        for i in range(W):
            original_dist = deepcopy(dist)
            dfs(n+1, bfs(i, num_brick))
            dist = original_dist

    # 처음 벽돌 수 세기
    cnt_brick = 0
    for h in range(H):
        for w in range(W):
            if brick[h][w] >= 1:
                cnt_brick += 1

    dfs(0, 0)
    
    print(f'#{t} {cnt_brick-max_brick}')

        
            
