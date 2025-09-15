# 같은 편 만들기

def make_set(n):
    parents = [i for i in range(n+1)]
    ranks = [0] * (n+1)
    return parents, ranks

def find_set(x):
    if x == parents[x]:
        return x

    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find_set(x)
    rep_y = find_set(y)

    if rep_x == rep_y:
        return

    # if rep_x < rep_y:
    #     parents[rep_y] = rep_x
    # else:
    #     parents[rep_x] = rep_y

    # 덩치가 더 작은 집합(rank가 더 낮은 집합)이 더 큰 집합 밑으로 들어간다.
    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        # rank가 동일
        # 한 쪽으로 병합하고 대표자의 rank를 +1
        parents[rep_y] = rep_x
        ranks[rep_x] += 1
 
N = 6
parents, ranks = make_set(N)
union(2, 4)
union(4, 6)

print(parents, ranks)