T = int(input())

for test_case in range(1, T + 1):

    # 5789. 현주의 상자 바꾸기
    N = int(input())
    numbers = [int(x) for x in input().split()]

    tree = [None] * (N+1)
    for i, n in enumerate(numbers):
        idx = i + 1
        tree[idx] = n
        print(tree)
        while True:
            if idx // 2 == 0:
                break
            else:
                if tree[idx // 2] > tree[idx]:
                    tree[idx // 2], tree[idx] = tree[idx], tree[idx // 2]
                idx = idx // 2
    
    print(tree)
    sum = 0
    idx = N
    while True:
        if idx // 2 == 0:
            break
        else:
            sum += idx[N]
        idx = idx // 2
    
    print(f'#{test_case} {sum}')


