T = int(input())

for test_case in range(1, T + 1):

    # 5174. subtree
    E, N = map(int, input().split())
    numbers = [int(x) for x in input().split()]

    tree_dict = {}

    for n in range(len(numbers)//2):
        parent, child = numbers[2*n], numbers[2*n+1]
        if parent not in tree_dict:
            tree_dict[parent] = [child]
        else:
            tree_dict[parent].append(child)
    
    queue = []
    sub_tree = set()
    start = N
    queue.append(start)
    while True:
        v = queue.pop(0)
        sub_tree.add(v)
        if v not in tree_dict:
            if len(queue) == 0:
                break
            else:
                continue
        else:
            for sub in tree_dict[v]:
                queue.append(sub)
    
    print(f'#{test_case} {len(sub_tree)}')