# 1717. 집합의 표현
N, M = map(int, input().split())

def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents, ranks

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return
    
    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        parents[rep_y] = rep_x
        ranks[rep_x] += 1

parents, ranks = make_set(N)

for _ in range(M):
    w, a, b = map(int, input().split())
    if w == 0:
        union(a, b)
    elif w == 1:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")