# 연산
from collections import deque

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    
    # 연산 횟수
    cnt = 0
    queue = deque()
    used = [False] * 1000001

    # 연산 시작
    queue.append(N)
    used[N] = True

    while True:
        cnt += 1
        for q in range(len(queue)):
            new_num = queue.popleft()
            # +1
            plus_1 = new_num + 1
            if plus_1 <= 1000000 and not used[plus_1]:
                used[plus_1] = True
                queue.append(plus_1)
            # -1
            minus_1 = new_num - 1
            if minus_1 >= 1 and not used[minus_1]:
                used[minus_1] = True
                queue.append(minus_1)
            # *2
            double = new_num * 2
            if double <= 1000000 and not used[double]:
                used[double] = True
                queue.append(double)
            # -10
            minus_10 = new_num - 10
            if minus_10 >= 1 and not used[minus_10]:
                used[minus_10] = True
                queue.append(minus_10)

        if used[M]:
            break
    
    print(f'#{t}', cnt)
        