T = int(input())

for test_case in range(1, T + 1):

    # 2805. 농작물 수확하기
    N = int(input())
    area = [[int(x) for x in input()] for y in range(N)]
    total = 0
    for i in range(N):
        if i <= N // 2:
            total += sum(area[i][N // 2 - i:N // 2 + 1 + i])
        else:
            total += sum(area[i][i - N // 2 :N - (i - N // 2)])

    print(f'#{test_case} {total}')