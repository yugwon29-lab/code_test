# 20058. 마법사 상어와 파이어스톰
from collections import deque

N, Q = map(int, input().split())
M = 2 ** N
A = [[int(x) for x in input().split()] for _ in range(M)]
L_list = [int(x) for x in input().split()]

# 시계 방향으로 90도 회전시킨다.
def rotate(L):
    B = [[0] * M for _ in range(M)]
    I = 2 ** L
    P = 2 ** (N - L)
    for i in range(P):
        for j in range(P):
            for r in range(I):
                for c in range(I):
                    B[r + I * i][c + I * j] = A[I * i + (I - 1 - c)][I * j + r]
    return B

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 얼음이 녹는다.
def melt(B):
    A = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            cnt_ice = 0
            for m in move:
                ni, nj = i + m[0], j + m[1]
                if not (0 <= ni < M and 0 <= nj < M):
                    continue
                if B[ni][nj] == 0:
                    continue
                cnt_ice += 1
            if cnt_ice < 3:
                A[i][j] = B[i][j] - 1
                if A[i][j] < 0:
                    A[i][j] = 0
            else:
                A[i][j] = B[i][j]
    return A

# 가장 큰 얼음 덩어리 칸 수와 전체 얼음 개수를 센다.
def big_ice(A):
    total_ice = 0
    max_cnt = 0
    visited = [[False] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            total_ice += A[i][j]
            ### 얼음 수 세기 ###
            if A[i][j] == 0:
                continue
            if visited[i][j]:
                continue
            si, sj = i, j
            q = deque()

            q.append((si, sj))
            visited[si][sj] = True
            cnt = 0

            while q:
                ii, jj = q.popleft()
                cnt += 1

                for m in move:
                    ni, nj = ii + m[0], jj + m[1]
                    if not (0 <= ni < M and 0 <= nj < M):
                        continue
                    if A[ni][nj] == 0 or visited[ni][nj]:
                        continue
                    visited[ni][nj] = True
                    q.append((ni, nj))
            
            if cnt > max_cnt:
                max_cnt = cnt

    return total_ice, max_cnt

for q in range(Q):
    B = rotate(L_list[q])
    A = melt(B)

total_ice, max_cnt = big_ice(A)

print(total_ice)
print(max_cnt)