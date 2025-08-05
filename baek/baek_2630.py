# 2630. 색종이 만들기

def is_same(paper):
    color = paper[0][0]
    length = len(paper)
    same = True
    for idx in range(length * length):
        if color != paper[idx // length][idx % length]:
            same = False
            break
    return same

# 하얀색, 파란색 종이 개수
cnt_paper = [0, 0]

def cut_paper(paper):
    global cnt_paper
    if is_same(paper):
        color = paper[0][0]
        cnt_paper[color] += 1
    else:
        length_div = len(paper) // 2

        cut_paper([[paper[y][x] for x in range(0, length_div)] for y in range(0, length_div)])
        cut_paper([[paper[y][x] for x in range(length_div, length_div * 2)] for y in range(0, length_div)])

        cut_paper([[paper[y][x] for x in range(0, length_div)] for y in range(length_div, length_div * 2)])
        cut_paper([[paper[y][x] for x in range(length_div, length_div * 2)] for y in range(length_div, length_div * 2)])

N = int(input())
paper = [[int(x) for x in input().split()] for y in range(N)]

cut_paper(paper)
print(cnt_paper[0])
print(cnt_paper[1])