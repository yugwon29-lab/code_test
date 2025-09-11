# 최소 생산 비용
T = int(input())

for t in range(1, T+1):
    N = int(input())

    min_cost = None
    complete = [False] * N
    cost_arr = [[int(x) for x in input().split()] for _ in range(N)]

    def make(cur, cost):
        global min_cost

        if cur == N:
            if min_cost is None or min_cost > cost:
                min_cost = cost
            return
        
        if min_cost is not None and min_cost <= cost:
            return
        
        for i in range(N):
            if not complete[i]:
                complete[i] = True
                make(cur+1, cost+cost_arr[cur][i])
                complete[i] = False
    
    make(0, 0)

    print(f'#{t}', min_cost)