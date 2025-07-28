T = 10

for test_case in range(1, T + 1):

    # 1220. Magnetic
    N = int(input())
    array = [[int(x) for x in input().split()] for _ in range(N)]

    cnt = 0
    switch = [False] * N

    for i in range(N):
        for j in range(N):
            if array[i][j] == 1 and not switch[j]:
                switch[j] = True
            elif array[i][j] == 2 and switch[j]:
                switch[j] = False
                cnt += 1

    print(f'#{test_case} {cnt}')