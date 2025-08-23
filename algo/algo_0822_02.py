# subtree

T = int(input())

for t in range(1, T+1):
    E, N = map(int, input().split())
    edges = [int(x) for x in input().split()]

    tree = [[0, 0] for _ in range(E+2)]
    for i in range(E):
        a, b = edges[2*i], edges[2*i+1]
        if tree[a][0] == 0:
            tree[a][0] = b
        elif tree[a][1] == 0:
            tree[a][1] = b

    node = 0
    def cnt_node(i):
        global node
        node += 1
        if tree[i][0] != 0:
            cnt_node(tree[i][0])
        if tree[i][1] != 0:
            cnt_node(tree[i][1])

    cnt_node(N)
    print(f'#{t} {node}')

    
