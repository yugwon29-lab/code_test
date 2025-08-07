# 색칠하기

T = int(input())

for t in range(1, T+1):
    N = int(input())
    array = [[0] * 10 for _ in range(10)]

    cnt_purple = 0  
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if array[r][c] != color and array[r][c] != 3:
                    array[r][c] += color
                    if array[r][c] == 3:
                        cnt_purple += 1
    
    print(f'#{t} {cnt_purple}')