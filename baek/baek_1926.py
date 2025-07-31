from collections import deque

# 1926. 그림

# 입력 받기
N, M = map(int, input().split())
picture = [[int(x) for x in input().split()] for _ in range(N)]

# check 배열
check = [[-1 for _ in range(M)] for _ in range(N)]

# 이동 경우의 수
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 그림 개수 및 가장 큰 넓이 체크
cnt, max_area = 0, 0

# 넓이 체크 함수
def get_area(start):
    area = 0
    queue = deque()
    check[start[0]][start[1]] = 0
    queue.append(start)

    while len(queue) != 0:
        i, j = queue.popleft()
        # 넓이 추가
        area += 1

        # 모든 이동 경우의 수 따지기
        for m in move:
            next_i, next_j = i + m[0], j + m[1]
            # 그림 밖이면 continue
            if (0 <= next_i < N) and (0 <= next_j < M):
                if picture[next_i][next_j] == 1 and check[next_i][next_j] == -1:
                    check[next_i][next_j] = 0
                    queue.append((next_i, next_j))
            else:
                continue

    return area

# 그림을 보면서 체크 안 된 그림이 있다면 그림 수 증가 및 넓이 구하기
for n in range(N):
    for m in range(M):
        if picture[n][m] == 1 and check[n][m] == -1:
            cnt += 1
            area = get_area((n, m))
            if area > max_area:
                max_area = area

print(cnt)
print(max_area)

