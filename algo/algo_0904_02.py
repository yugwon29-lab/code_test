# 최소합
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for _ in range(N)]

    min_sum = None

    def move(i, j, total):
        global min_sum

        if (i, j) == (N-1, N-1):
            if min_sum is None or min_sum > total:
                min_sum = total
            return

        if min_sum is not None and min_sum < total:
            return
        
        for di, dj in [(1, 0), (0, 1)]:
            ni, nj = i + di, j + dj
            if (0 <= ni < N) and (0 <= nj < N):
                move(ni, nj, total+arr[ni][nj])

    move(0, 0, arr[0][0])

    print(f'#{t} {min_sum}')