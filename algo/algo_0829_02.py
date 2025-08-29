# 이진 힙

T = int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = [int(x) for x in input().split()]

    tree = [0] * (N+1)
    idx = 1

    def in_heap(k, num):
        tree[k] = num

        while True:
            p = k // 2
            if p == 0:
                break
            if tree[p] > tree[k]:
                tree[k], tree[p] = tree[p], tree[k]
                k = k // 2
            else:
                break

    for i in range(N):
        in_heap(i+1, numbers[i])
    
    total = 0
    k = N
    while True:
        p = k // 2
        if p == 0:
            break
        total += tree[p]
        k = k // 2
        
    print(f'#{t} {total}')