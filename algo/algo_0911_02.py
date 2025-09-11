# 전기버스2
T = int(input())

for t in range(1, T+1):
    N, *stop = map(int, input().split())
    stop += [0]

    min_k = 1000
    def go(cur, k):
        global min_k
        if cur == N-1:
            if min_k > k:
                min_k = k
            return
        
        if min_k <= k:
            return
        
        for i in range(1, stop[cur]+1):
            if cur+i >= N:
                continue
            go(cur+i, k+1)

    go(0, -1)
    print(f'#{t}', min_k)