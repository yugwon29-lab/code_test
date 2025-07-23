T = int(input())

for i in range(1, T + 1):

    # 4861.회문
    N, M = map(int, input().split())
    a = [[x for x in input()] for y in range(N)]

    # 가로줄 탐색
    for m in range(N):
        for n in range(N-M+1):
            same = True
            for k in range(M // 2):
                if a[m][n+k] != a[m][n+M-1-k]:
                    same = False
                    break
            if same:
                print(f"#{i} {''.join(a[m][n:n+M])}")
                break
        if same:
            break
    
    # 세로줄 탐색
    for m in range(N-M+1):
        for n in range(N):
            same = True
            for k in range(M // 2):
                if a[m+k][n] != a[m+M-1-k][n]:
                    same = False
                    break
            if same:
                print(f"#{i} {''.join([a[x][n] for x in range(m, m+M)])}")
                break
        if same:
            break