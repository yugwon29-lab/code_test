# 사칙연산

T = 10

for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    child = [0] * (N+1)

    for i in range(N):
        li = input().split()

        if len(li) == 2:
            n, v = int(li[0]), int(li[1])
            tree[n] = v
        elif len(li) == 4:
            n, v, c1, c2 = int(li[0]), li[1], int(li[2]), int(li[3])
            tree[n] = v
            child[n] = (c1, c2)

    def cal(node):
        if tree[node] == "+":
            return cal(child[node][0]) + cal(child[node][1])
        elif tree[node] == "-":
            return cal(child[node][0]) - cal(child[node][1])
        elif tree[node] == "*":
            return cal(child[node][0]) * cal(child[node][1])
        elif tree[node] == "/":
            return cal(child[node][0]) / cal(child[node][1])
        else:
            return tree[node]

    result = int(cal(1))
    print(f'#{t} {result}')
    