# 이진탐색

T = int(input())

for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    
    num = 1
    def inorder(i):
        global num
        if 1 <= 2*i <= N:
            inorder(2*i)
        tree[i] = num
        num += 1
        if 1 <= 2*i+1 <= N:
            inorder(2*i+1)

    inorder(1)

    print(f'#{t} {tree[1]} {tree[N//2]}')