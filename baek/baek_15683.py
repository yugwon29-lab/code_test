import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = {
    1: [[(1,0)], [(-1,0)], [(0,1)], [(0,-1)]],
    2: [[(1,0),(-1,0)], [(0,1),(0,-1)]],
    3: [[(-1,0),(0,1)], [(0,1),(1,0)], [(1,0),(0,-1)], [(0,-1),(-1,0)]],
    4: [[(0,-1),(-1,0),(0,1)], [(-1,0),(0,1),(1,0)],
        [(0,1),(1,0),(0,-1)], [(1,0),(0,-1),(-1,0)]],
    5: [[(1,0),(-1,0),(0,1),(0,-1)]]
}

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctvs.append((i, j, board[i][j]))

ans = N * M

def watch(temp, x, y, moves):
    for dx, dy in moves:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if not (0 <= nx < N and 0 <= ny < M): 
                break
            if temp[nx][ny] == 6: 
                break  # 벽이면 멈춤
            if temp[nx][ny] == 0:  # 빈 칸만 감시 처리
                temp[nx][ny] = -1

def dfs(idx, board_now):
    global ans
    if idx == len(cctvs):
        cnt = sum(row.count(0) for row in board_now)
        ans = min(ans, cnt)
        return

    x, y, t = cctvs[idx]
    for moves in dirs[t]:
        temp = copy.deepcopy(board_now)
        watch(temp, x, y, moves)
        dfs(idx+1, temp)

dfs(0, board)
print(ans)
