# 화물 도크
T = int(input())

for t in range(1, T+1):
    N = int(input())
    tasks = []

    # 가장 빨리 끝나는 작업을 우선적으로 선택한다.
    for _ in range(N):
        s, e = map(int, input().split())
        tasks.append((e, s))
    
    tasks.sort()

    cnt = 0
    idx = 0
    end_time = -1

    while idx < N:
        now_task = tasks[idx]
        # 현재 작업을 할 수 있을 경우
        if now_task[0] >= end_time and now_task[1] >= end_time:
            end_time = now_task[0]
            cnt += 1
        idx += 1
    
    print(f'#{t} {cnt}')