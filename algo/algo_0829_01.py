# 노드의 합

T = int(input())

for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        k, v = map(int, input().split())
        tree[k] = v

    def add_node(node):
        global tree
        if node * 2 + 1 <= N:
            tree[node] = add_node(node*2) + add_node(node*2 + 1)
        elif node * 2 <= N:
            tree[node] = tree[node*2]

        return tree[node]
    
    add_node(1)
    print(f'#{t} {tree[L]}')