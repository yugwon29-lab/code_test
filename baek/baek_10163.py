# 10163. 색종이

N = int(input())
paper = []
for _ in range(N):
    x1, y1, width, height = map(int, input().split())
    paper.append((x1, y1, width, height))

paper_cnt = [0] * N
big_paper = [[-1] * 1001 for _ in range(1001)]

for i in range(N-1, -1, -1):
    xn, yn, wn, hn = paper[i]
    for r in range(yn, yn + hn):
        for c in range(xn, xn + wn):
            if big_paper[r][c] == -1:
                big_paper[r][c] = i
                paper_cnt[i] += 1

for ans in paper_cnt:
    print(ans)