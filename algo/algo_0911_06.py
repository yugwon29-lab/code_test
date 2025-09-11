# 동철이의 일 분배
T = int(input())

for t in range(1, T+1):
    N = int(input())
    percent = [[int(x)/100 for x in input().split()] for _ in range(N)]

    selected = [False] * N

    max_percent = 0
    def work(cur, pc):
        global max_percent
        if cur == N:
            if pc > max_percent:
                max_percent = pc
            return
        
        if pc <= max_percent:
            return
        
        for i in range(N):
            if not selected[i]:
                selected[i] = True
                work(cur+1, pc * percent[cur][i])
                selected[i] = False

    work(0, 1.0)
    print(f'#{t} {max_percent * 100:.6f}')