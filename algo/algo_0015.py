# 연습 문제 16
# 전위 순회하여 정점의 번호를 출력한다.

V = int(input())
edges = [int(x) for x in input().split()]
tree = [[-1, -1] for _ in range(V+1)]
print(tree)

for i in range(V-1):
    a, b = edges[2*i], edges[2*i+1]
    if tree[a][0] == -1:
        tree[a][0] = b
    elif tree[a][1] == -1:
        tree[a][1] = b

def preorder(T):
    print(T)
    if tree[T][0] != -1:
        preorder(tree[T][0])
    if tree[T][1] != -1:
        preorder(tree[T][1])

preorder(1)