# 2105. 디저트 카페

T = int(input())

for t in range(1, T+1):
    N = int(input())
    cafe = [[int(x) for x in input().split()] for _ in range(N)]

    max_dessert = -1

    dessert_list = []
    def go_cafe(i, j, d, m0, m1, m2, m3, dessert_list):
        global max_dessert, si, sj

        if (i, j) == (si, sj) and d == 3 and m0 == m2 and m1 == m3:
            if len(dessert_list) > max_dessert:
                max_dessert = len(dessert_list)
            return
        
        if d == 0:
            if 0 <= i+1 < N and 0 <= j+1 < N:
                if cafe[i+1][j+1] not in dessert_list:
                    go_cafe(i+1, j+1, d, m0+1, m1, m2, m3, dessert_list+[cafe[i+1][j+1]])
            if m0 != 0 and 0 <= i+1 < N and 0 <= j-1 < N:
                if cafe[i+1][j-1] not in dessert_list:
                    go_cafe(i+1, j-1, 1, m0, m1+1, m2, m3, dessert_list+[cafe[i+1][j-1]])
        elif d == 1:    
            if 0 <= i+1 < N and 0 <= j-1 < N:
                if cafe[i+1][j-1] not in dessert_list:
                    go_cafe(i+1, j-1, d, m0, m1+1, m2, m3, dessert_list+[cafe[i+1][j-1]])
            if m1 != 0 and 0 <= i-1 < N and 0 <= j-1 < N:
                if cafe[i-1][j-1] not in dessert_list:
                    go_cafe(i-1, j-1, 2, m0, m1, m2+1, m3, dessert_list+[cafe[i-1][j-1]])
        elif d == 2:
            if m2 < m0:
                if 0 <= i-1 < N and 0 <= j-1 < N:
                    if cafe[i-1][j-1] not in dessert_list:
                        go_cafe(i-1, j-1, d, m0, m1, m2+1, m3, dessert_list+[cafe[i-1][j-1]])
            else:
                if 0 <= i-1 < N and 0 <= j+1 < N:
                    if cafe[i-1][j+1] not in dessert_list:
                        go_cafe(i-1, j+1, 3, m0, m1, m2, m3+1, dessert_list+[cafe[i-1][j+1]])
        else:
            if 0 <= i-1 < N and 0 <= j+1 < N:
                if cafe[i-1][j+1] not in dessert_list:
                    go_cafe(i-1, j+1, d, m0, m1, m2, m3+1, dessert_list+[cafe[i-1][j+1]])

    for i in range(N):
        for j in range(N):
            si, sj = i, j
            go_cafe(i, j, 0, 0, 0, 0, 0, [])

    print(f'#{t} {max_dessert}')