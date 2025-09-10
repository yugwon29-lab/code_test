# 15685. 드래곤 커브
N = int(input())

board = [[False] * 101 for _ in range(101)]

dir_dict = {
    0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)
}

def dragon_curve(x, y, d, g):
    directions = [d]
    for gg in range(g):
        new_direction = []
        num_dir = len(directions)
        for idx in range(num_dir-1, -1, -1):
            now_dir = directions[idx]
            new_direction.append((now_dir + 1) % 4)
        directions += new_direction
    
    board[y][x] = True
    ny, nx = y, x
    for dir in directions:
        nx, ny = nx + dir_dict[dir][1], ny + dir_dict[dir][0]
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            board[ny][nx] = True 

for _ in range(N):
    X, Y, D, G = map(int, input().split())
    dragon_curve(X, Y, D, G)

total = 0
for i in range(100):
    for j in range(100):
        rect = True
        for r in range(2):
            for c in range(2):
                if not board[i+r][j+c]:
                    rect = False
        if rect:
            total += 1

print(total)