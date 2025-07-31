from collections import deque

# 1697. 숨바꼭질

# 입력 받기
N, K = map(int, input().split())

# 시작점
start = N

# 이동 경우의 수
move = [1, -1, 'x2']

# BFS
queue = deque()

# 수빈이 간 지점 확인하기
check = {start: 0}

queue.append(start)
while len(queue) != 0:
    i = queue.popleft()
    # 동생을 찾았다면,
    if i == K:
        break
    
    # 이동 경로 탐색
    for m in move:
        if m == 'x2':
            next_i = i * 2
        else:
            next_i = i + m

        # 지나가지 않은 곳이면, 그리고 범위 내이면,
        if next_i not in check and 0 <= next_i <= 100000:
            check[next_i] = check[i] + 1
            queue.append(next_i)

print(check[K])