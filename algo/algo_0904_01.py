# 전자카트

T = int(input())

for t in range(1, T+1):
    N = int(input())
    battery = [[int(x) for x in input().split()] for _ in range(N)]

    visited = [False] * N

    min_charge = None

    def visit(cur, charge, i):
        global min_charge

        # 종료 조건
        if cur == N - 1:
            # 사무실로 돌아가기
            charge += battery[i][0]
            if min_charge is None or min_charge > charge:
                min_charge = charge
            return
        
        # 가지치기
        if min_charge is not None and charge > min_charge:
            return
        
        for j in range(1, N):
            if not visited[j]:
                visited[j] = True
                visit(cur+1, charge+battery[i][j], j)
                visited[j] = False
        
    visit(0, 0, 0)

    print(f'#{t} {min_charge}')