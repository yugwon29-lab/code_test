# 중위순회

T = 10

for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(N):
        new_in = input().split()
        if len(new_in) == 2:
            i, c = int(new_in[0]), new_in[1]
        elif len(new_in) == 3:
            i, c, ch1 = int(new_in[0]), new_in[1], int(new_in[2])
        elif len(new_in) == 4:
            i, c, ch1, ch2 = int(new_in[0]), new_in[1], int(new_in[2]), int(new_in[3])
        tree[i] = c
    
    def inorder(i):
        if 1 <= 2*i <= N:
            inorder(2*i)
        print(tree[i], end='')
        if 1 <= 2*i+1 <= N:
            inorder(2*i+1)

    print(f'#{t}', end=' ')
    inorder(1)
    print()