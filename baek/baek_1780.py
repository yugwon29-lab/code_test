# 1780. 종이의 개수

def is_same(paper):
    num = None
    length = len(paper)
    same = True
    for idx in range(length * length):
        if num is None:
            num = paper[idx // length][idx % length]
        else:
            if num != paper[idx // length][idx % length]:
                same = False
                break

    return same


# 각각 0, 1, -1의 개수
num_paper = [0, 0, 0]


def cut_paper(paper):
    global num_paper
    if is_same(paper):
        num_paper[paper[0][0]] += 1
    else:
        length_thr = len(paper) // 3
        cut_paper([[paper[y][x] for x in range(0, length_thr)] for y in range(0, length_thr)])
        cut_paper([[paper[y][x] for x in range(length_thr, length_thr * 2)] for y in range(0, length_thr)])
        cut_paper([[paper[y][x] for x in range(length_thr * 2, length_thr * 3)] for y in range(0, length_thr)])

        cut_paper([[paper[y][x] for x in range(0, length_thr)] for y in range(length_thr, length_thr * 2)])
        cut_paper([[paper[y][x] for x in range(length_thr, length_thr * 2)] for y in range(length_thr, length_thr * 2)])
        cut_paper([[paper[y][x] for x in range(length_thr * 2, length_thr * 3)] for y in range(length_thr, length_thr * 2)])

        cut_paper([[paper[y][x] for x in range(0, length_thr)] for y in range(length_thr * 2, length_thr * 3)])
        cut_paper([[paper[y][x] for x in range(length_thr, length_thr * 2)] for y in range(length_thr * 2, length_thr * 3)])
        cut_paper([[paper[y][x] for x in range(length_thr * 2, length_thr * 3)] for y in range(length_thr * 2, length_thr * 3)])


# 입력 받기
N = int(input())
paper = [[int(x) for x in input().split()] for _ in range(N)]

cut_paper(paper)
print(num_paper[-1])
print(num_paper[0])
print(num_paper[1])