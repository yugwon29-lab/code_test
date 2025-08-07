# 파리퇴치

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    flies = [[int(x) for x in input().split()] for _ in range(N)]
    
    max_flies = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            catch_flies = 0
            for i in range(M):
                for j in range(M):
                    catch_flies += flies[r+i][c+j]
            if max_flies < catch_flies:
                max_flies = catch_flies
    
    print(f'#{t} {max_flies}')
