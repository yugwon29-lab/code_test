T = int(input())

for test_case in range(1, T + 1):

    # 5177. 이진 힙
    N = int(input())
    numbers = [int(x) for x in input().split()]

    tree = [None] * (N+1)
    for i, n in enumerate(numbers):
        idx = i + 1
        tree[idx] = n
        while True:
            if idx // 2 == 0:
                break
            else:
                if tree[idx // 2] > tree[idx]:
                    tree[idx // 2], tree[idx] = tree[idx], tree[idx // 2]
                idx = idx // 2
    
    # print(tree)
    
    idx = N // 2
    sum = 0

    while True:
        if idx == 0:
            break
        else:
            sum += tree[idx]
        idx = idx // 2
    
    print(f'#{test_case} {sum}')


