# 부분 수열의 합
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]

    used = [False] * N

    cnt = 0
    def sum(idx, total):
        global cnt
        if idx == N:
            if total == K:
                cnt += 1
            return
        
        sum(idx+1, total)
        sum(idx+1, total+A[idx])

    sum(0, 0)
    print(f'#{t}', cnt)