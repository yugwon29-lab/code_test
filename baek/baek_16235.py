# 16235. 나무 재테크
from collections import deque

N, M, K = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(N)]
B = [[5] * N for _ in range(N)]

trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

# 정렬
for y in range(N):
    for x in range(N):
        sorted(trees[y][x])

move = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

for _ in range(K):
    # 봄
    dead_trees = [[deque() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            live_trees = deque()
            for tree in trees[i][j]:
                # 나무 양분을 먹을 수 없다면 즉시 아웃
                if tree > B[i][j]:
                    dead_trees[i][j].append(tree)
                else:
                    B[i][j] -= tree
                    tree += 1
                    live_trees.append(tree)
            trees[i][j] = live_trees
    
    # 여름
    for i in range(N):
        for j in range(N):
            for tree in dead_trees[i][j]:
                B[i][j] += tree // 2
    
    # 가을
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                # 나무 나이가 5의 배수이면, 번식
                if tree % 5 == 0:
                    for m in move:
                        ni, nj = i + m[0], j + m[1]
                        if 0 <= ni < N and 0 <= nj < N:
                            trees[ni][nj].appendleft(1)
    
    # 겨울
    for i in range(N):
        for j in range(N):
            B[i][j] += A[i][j]

total = 0
for i in range(N):
    for j in range(N):
        total += len(trees[i][j])

print(total)


