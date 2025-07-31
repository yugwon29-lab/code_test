from collections import deque

# 5014. 스타트링크

# 입력 받기
F, S, G, U, D = map(int, input().split())

# 딕셔너리
visited = {}

# 이동할 수 있는 경우의 수
move = [U, -D]

# 시작점
visited[S] = 0

queue = deque()
queue.append(S)

while len(queue) != 0:
    now_floor = queue.popleft()
    if now_floor == G:
        break

    for m in move:
        next_floor = now_floor + m
        if 1 <= next_floor <= 1000000 and next_floor <= F:
            if next_floor not in visited:
                visited[next_floor] = visited[now_floor] + 1
                queue.append(next_floor)
        else:
            continue

if G not in visited:
    print('use the stairs')
else:
    print(visited[G])