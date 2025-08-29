# 힙

T = int(input())

for t in range(1, T+1):
    N = int(input())
    tree = [0] * 100001
    elem = 0
    result = []

    def in_tree(num):
        global tree, elem
        # 요소 추가
        elem += 1
        tree[elem] = num
        k = elem
        while True:
            p = k // 2
            if p == 0:
                break
            if tree[p] > tree[k]:
                break
            tree[p], tree[k] = tree[k], tree[p]
            k = k // 2

    def out_tree():
        global tree, elem, result
        if tree[1] == 0:
            result.append(-1)
        else:
            result.append(tree[1])
            tree[1], tree[elem] = tree[elem], 0
            elem -= 1
            k = 1
            while True:
                a = k * 2 if k * 2 <= elem else 0
                b = k * 2 + 1 if k * 2 + 1 <= elem else 0
                if tree[a] > tree[b]:
                    if tree[k] < tree[a]:
                        tree[k], tree[a] = tree[a], tree[k]
                        k = a
                    else:
                        break
                elif tree[a] < tree[b]:
                    if tree[k] < tree[b]:
                        tree[k], tree[b] = tree[b], tree[k]
                        k = b
                    else:
                        break
                else:
                    break
    
    for _ in range(N):
        li = input().split()
        if len(li) == 2:
            in_tree(int(li[1]))
        else:
            out_tree()
    
    print(f'#{t}', end=' ')
    print(*result)