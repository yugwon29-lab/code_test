# 21610. 마법사 상어와 비바라기
N, M = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(N)]
moves = []
for _ in range(M):
    d, s = map(int, input().split())
    moves.append((d, s))

# 초기 구름
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 방향 사전
direct = {
    1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
    5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)
}

# 물복사 버그 방향
copy_d = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

# M번의 마법 실행
for m in range(M):
    d, s = moves[m]

    cloud_board = [[False] * N for _ in range(N)]
    for r, c in clouds:
        dr, dc = direct[d]
        nr, nc = (r + dr * s) % N, (c + dc * s) % N

        # 구름에서 비가 내려 1만큼 물이 내림.
        A[nr][nc] += 1
        # 구름이 사라진 칸 표시
        cloud_board[nr][nc] = True
    
    clouds.clear()

    # 물이 증가한 칸에서 물복사버그 마법 시전
    for r in range(N):
        for c in range(N):
            if cloud_board[r][c]:
                cnt_water = 0
                for dr, dc in copy_d:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if A[nr][nc] > 0:
                        cnt_water += 1
                # 물복사버그 마법
                A[r][c] += cnt_water

    # 물의 양이 2 이상이 모든 칸에 구름이 생기고 물의 양 2만큼 줄어들기
    for r in range(N):
        for c in range(N):
            if not cloud_board[r][c]:
                if A[r][c] >= 2:
                    clouds.append((r, c))
                    A[r][c] -= 2

total_water = 0
for r in range(N):
    for c in range(N):
        total_water += A[r][c]

print(total_water)