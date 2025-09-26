# 21611. 마법사 상어와 블리자드
N, M = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(N)]
magic = []
for _ in range(M):
    d, s = map(int, input().split())
    magic.append((d, s))

# 상어의 위치
SR, SC = N // 2, N // 2

# 방향 딕셔너리
direct = {
    1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)
}

for m in range(M):
    d, s = magic[m]
    dr, dc = direct[d]

    # 구슬 파괴
    for ds in range(s):
        ni, nj = SR + ds