# 2563. 색종이

N = int(input())
paper = []
for _ in range(N):
    x1, y1 = map(int, input().split())
    paper.append((x1, y1))

big_paper = [[0] * 100 for _ in range(100)]
black_area = 0

for i in range(N):
    x, y = paper[i]
    for r in range(y, y+10):
        for c in range(x, x+10):
            if big_paper[r][c] == 0:
                big_paper[r][c] = 1
                black_area += 1

print(black_area)