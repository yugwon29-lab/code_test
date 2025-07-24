T = int(input())

for test_case in range(1, T + 1):

    # 5176. 이진탐색
    N = int(input())

    tree = [None] * (N+1)
    num = 1

    def number_tree(tree, idx=1):
        global num

        # 왼쪽 트리부터 확인
        if idx * 2 < len(tree):
            number_tree(tree, idx * 2)
        tree[idx] = num
        num += 1
        if idx * 2 + 1 < len(tree):
            number_tree(tree, idx * 2 + 1)


    number_tree(tree, 1)

    print(f'#{test_case} {tree[1]} {tree[N//2]}')