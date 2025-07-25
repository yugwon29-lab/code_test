T = int(input())

for test_case in range(1, T + 1):

    # 5178. 노드의 합
    N, M, L = map(int, input().split())

    # 이진 트리 생성
    tree = [None] * (N + 1)

    for i in range(M):
        leap, num = map(int, input().split())
        tree[leap] = num

    def add_node(idx=1):
        # 왼쪽 노드 확인
        if idx * 2 < len(tree):
            add_node(idx * 2)
        # 오른쪽 노드 확인
        if idx * 2 + 1 < len(tree):
            add_node(idx * 2 + 1)
        # 중앙 노드 구하기
        if tree[idx] is None:
            if idx * 2 + 1 < len(tree):
                tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
            else:
                tree[idx] = tree[idx * 2]

    add_node(1)

    print(f'#{test_case} {tree[L]}')